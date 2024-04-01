import json
import os
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader, Docx2txtLoader, CSVLoader, UnstructuredExcelLoader, \
    UnstructuredPowerPointLoader, UnstructuredPDFLoader
from qdrant_client import qdrant_client
from logger import vdb_logger, vdb_debug_logger
from constants import YOUR_OPENAI_API_KEY


os.environ["OPENAI_API_KEY"] = YOUR_OPENAI_API_KEY

class VectorStore:  # заполнение вбд
        

    def load_to_db(self, file_name, cases_path):
        vdb_logger.info('START: load to db')
        self.read_and_handle_config()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
        documents = self.load_doc(file_name, cases_path)
        documents.metadata["path"] = cases_path
        split_docs = splitter.create_documents([documents.page_content], [documents.metadata])
        if not split_docs:
            vdb_logger.warning(f'{file_name} is empty')
            vdb_logger.info('END: load to db')
            return
        else:
            self.update_qd(split_docs)
            vdb_logger.info(f'{file_name} was added')
            vdb_logger.info('END: load to db')
            return


    def update_qd(self, docs):  # передает chunks в вбд
        vdb_logger.info('START: update qd')
        vdb_debug_logger.debug(f'update qd documents {docs=}')

        global qd
        if 'qd' in globals():
            qd.add_documents(docs)
        else:
            qd = Qdrant.from_documents(
                docs,
                OpenAIEmbeddings(),
                path=self.vdb_folder_path,
                collection_name=self.collection_name,
            )

        vdb_logger.info('END: update qd')

        return qd

    def load_doc(self, file_name, cases_path):  # читает документы с диска
        vdb_logger.info('START: load_doc')

        extension = os.path.splitext(file_name)[1]
        vdb_debug_logger.debug(f'load_doc {file_name=}, {extension=}')
        match extension:
            case ".txt":
                loader = TextLoader(file_path=f"{cases_path}{file_name}", autodetect_encoding=True)
            case ".docx" | ".doc":
                loader = Docx2txtLoader(file_path=f"{cases_path}{file_name}")
            case ".csv":
                loader = CSVLoader(file_path=f"{cases_path}{file_name}")
            case ".xlsx" | ".xls":
                loader = UnstructuredExcelLoader(file_path=f"{cases_path}{file_name}")
            case ".pptx" | ".ppt":
                loader = UnstructuredPowerPointLoader(file_path=f"{cases_path}{file_name}")
            case ".pdf":
                loader = UnstructuredPDFLoader(file_path=f"{cases_path}{file_name}")
            case _:
                vdb_logger.warning(f'{file_name} has an invalid extension')
                vdb_logger.info('END: load_doc')
                return

        documents = loader.load()[0]

        vdb_logger.info('END: load_doc')
        vdb_debug_logger.debug(f'load_doc {documents}')

        return documents

    def load_from_vdb(self, retrived_docs):  # форматирует адрес для функции чтнения доков
        vdb_logger.info('START: load_from_vdb')

        for ret in retrived_docs:
            cases_path = ret.metadata['source'].rsplit('/', 1)[0] + "/"
            file_name = ret.metadata['source'].rsplit('/', 1)[1]
            ret.page_content = self.load_doc(file_name, cases_path).page_content
            vdb_logger.info(f'{file_name} was loaded')

        vdb_logger.info('END: load_from_vdb')
        return retrived_docs

    def query(self, request):  # запрос в вбд
        
        vdb_logger.info('START: vdb query')
        self.read_and_handle_config()
        
        vdb_debug_logger.debug(f'vdb query {request=}')

        if self.connect_vdb():
            retriever = qd.as_retriever(search_kwargs={'k': 5})
            retrieved_docs = retriever.get_relevant_documents(request)
            retrieved_docs = self.load_from_vdb(retrieved_docs)

            vdb_logger.info('END: vdb query')

            return retrieved_docs

        vdb_logger.warning('can not connect to vdb')
        vdb_logger.info('END: vdb query')

        return []

    def connect_vdb(self):  # подключение к уже созданной вбд
        vdb_logger.info('START: connect to vdb')

        global qd
        if 'qd' not in globals():
            if os.path.exists(self.vdb_folder_path + "/collection/" + self.collection_name + "/"):
                client = qdrant_client.QdrantClient(
                    path=self.vdb_folder_path, prefer_grpc=True
                )
                qd = Qdrant(
                    client=client, collection_name=self.collection_name,
                    embeddings=OpenAIEmbeddings()
                )
            else:
                vdb_logger.warning(f'{self.collection_name} does not exist')
                vdb_logger.info('END: connect to vdb')
                return None

        vdb_logger.info('END: connect to vdb')

        return qd

    def get_path_config(self):
        current_vdb_path = os.path.abspath(__file__)
        vdb_path_components = current_vdb_path.split(os.path.sep)
        # path of main repository
        backend_index = vdb_path_components.index('Development-of-a-digital-twin-using-artificial-intelligence-methods')
        backend_path = os.path.sep.join(vdb_path_components[:backend_index + 1])
        self.config_file_path = os.path.join(backend_path, "vdb_config.json")
        return

    def read_and_handle_config(self):
        self.get_path_config()
        with open(self.config_file_path, "r") as json_file:
            data = json.load(json_file)
        self.vdb_folder_path=data["vdb_folder_path"]
        self.collection_name=data["collection_name"]
        return


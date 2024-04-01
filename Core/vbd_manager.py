import json
import os
from load_folder import CasesOnDrive
import vdb

class VDBManager:
    def __init__(self):
        self.json_file_path = "vdb_config.json"

    def check_config_existence(self):
        return os.path.exists(self.json_file_path) and os.path.isfile(self.json_file_path)

    def create_config(self):
        vdb_parameters = {
            "vdb_folder_path": "C:/YOUR_PATH_case_resources/local_qdrant",
            "collection_name": "cases_collection_YOUR_NAME",
            "case_path": "C:/YOUR_PATH_case_resources/cases/",
            "uploaded_cases_json": "C:/YOUR_PATH_case_resources/last_updated_cases_info.json",
            "NeededInitilaze": False
        }
        with open(self.json_file_path, "w") as json_file:
            json.dump(vdb_parameters, json_file, indent=4)
        return

    def read_and_handle_config(self):
        with open(self.json_file_path, mode='r') as json_file:
            data = json.load(json_file)

        if data.get("NeededInitilaze", True):
            v = CasesOnDrive()
            v.load_from_local(data["case_path"], data["uploaded_cases_json"])
            data['NeededInitilaze'] = False
            with open(self.json_file_path,"w") as json_file_for_write:
                json.dump(data, json_file_for_write)
            exit()

    def run_manager(self):
        if not self.check_config_existence():
            print("create json")
            self.create_config()
            exit()
        print(self.check_config_existence())

        self.read_and_handle_config()

## Example use bd
# VDBManager().run_manager()
# vbd = vdb.VectorStore()
# query = 'мечта'
# products_from_vbd = vbd.query(query)
# nomber_key = 0
# products = {}
# for product_from_vbd in products_from_vbd:
#     products[nomber_key] = product_from_vbd.page_content
#     nomber_key += 1

# txt_path = "result_vdb.txt"
# for i, chunk in enumerate(products.values()):
#         new_file_path = f"{os.path.splitext(txt_path)[0]}_{i+1}{os.path.splitext(txt_path)[1]}"
#         with open(new_file_path, 'w', encoding='utf-8') as new_file:
#             new_file.write(chunk)
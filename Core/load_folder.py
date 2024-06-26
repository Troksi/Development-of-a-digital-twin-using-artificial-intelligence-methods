import json
import os
from datetime import datetime
import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from vdb import VectorStore
from logger import vdb_logger, vdb_debug_logger
from Utiles.pause4limit import PauseForLimit

class CasesOnDrive:
    
    def load_from_local(self, cases_path, uploaded_cases_json):
        vdb_logger.info(f'START: load_from_local from {cases_path}')

        # Получаем список новых файлов
        docstorage_files = self.check_and_update_files_info(cases_path, uploaded_cases_json, update_json=False)
        pauseForLimit = PauseForLimit(2, 61)
        
        try:
            if docstorage_files:
                for file_name in docstorage_files:
                    pauseForLimit.reg_stap()
                    VectorStore().load_to_db(file_name, cases_path)
                    vdb_debug_logger.debug(f'file {file_name} was loaded')

                    # После загрузки файла обновляем JSON файл
                    self.update_json_with_file(uploaded_cases_json, file_name)
            else:
                vdb_logger.warning('no new files found')
                vdb_debug_logger.debug(f'no new files found {cases_path}')
            
            vdb_logger.info(f'END: load_from_local from {cases_path}')
        except Exception as ex:
            vdb_logger.error(f'file {file_name} was not loaded')
            vdb_logger.error(f'{ex}')
        return

    def check_and_update_files_info(self, cases_path, uploaded_cases_json, update_json=True):
        vdb_logger.info('START: check_and_update_files_info')

        if not os.path.exists(uploaded_cases_json):
            vdb_logger.warning('uploaded_cases_json was not found')
            vdb_debug_logger.debug(f'creating uploaded_cases_json {cases_path=}, {uploaded_cases_json=}')

            with open(uploaded_cases_json, 'w') as f:
                json.dump({"last_updated": None, "files": []}, f)

        with open(uploaded_cases_json, 'r') as f:
            vdb_logger.info(f'reading {uploaded_cases_json=}')
            uploaded_cases = json.load(f)

        current_cases_folder = set(os.listdir(cases_path))
        uploaded_cases_folder = set(uploaded_cases["files"])

        unuploaded_cases = current_cases_folder - uploaded_cases_folder
        uploaded_cases["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vdb_debug_logger.debug(f'{current_cases_folder=}, {uploaded_cases_folder=}, {unuploaded_cases=}')

        if unuploaded_cases and update_json:
            uploaded_cases["files"].extend(unuploaded_cases)
            with open(uploaded_cases_json, 'w') as f:
                vdb_logger.info('loading uploaded_cases')
                json.dump(uploaded_cases, f, indent=4)
            vdb_debug_logger.debug(f'{uploaded_cases=}')
        
        vdb_logger.info('END: check_and_update_files_info')
        return list(unuploaded_cases) if unuploaded_cases else None

    def update_json_with_file(self, uploaded_cases_json, file_name):
        with open(uploaded_cases_json, 'r') as f:
            uploaded_cases = json.load(f)

        uploaded_cases["files"].append(file_name)
        uploaded_cases["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(uploaded_cases_json, 'w') as f:
            json.dump(uploaded_cases, f, indent=4)
        
        vdb_logger.info(f'Updated {uploaded_cases_json} with {file_name}')

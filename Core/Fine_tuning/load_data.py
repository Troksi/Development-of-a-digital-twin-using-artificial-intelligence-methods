import openai 
import sys
import os 

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_dir)

from Utiles.select_file import  select_file_or_directory
from Core.constants import YOUR_OPENAI_API_KEY
from Core.logger import fine_tune_logger
from pathlib import Path



def get_filename_from_path(file_path):
    # Создаем объект Path
    path = Path(file_path).resolve()
    # Возвращаем имя файла без суффикса (расширения)
    return path.stem


class Load_data:
  openai_key = YOUR_OPENAI_API_KEY

  def __init__(self, openai_key=openai_key):
    self.openai_key = openai_key
    openai.api_key = self.openai_key
  
  def get_name(self):
    return "Load_data"

  def run(self):
    try:
      path_jsonl = select_file_or_directory()
      purpose_file = get_filename_from_path(path_jsonl)
      data_response = openai.File.create(
        file=open(path_jsonl, "rb"),
        purpose=purpose_file
      )
      fine_tune_logger.info(f'load file: {data_response} \n from path: {path_jsonl}')
      print(data_response)
    except Exception as ex:
      fine_tune_logger.error(f'error with file: {path_jsonl}\n error: {ex}')


if __name__ == "__main__":
  load_data = Load_data()
  load_data.run()


# from openai import OpenAI
# client = OpenAI()

# client.files.create(
#   file=open("mydata.jsonl", "rb"),
#   purpose="fine-tune"
# )
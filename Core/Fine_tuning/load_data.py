import openai
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_dir)

from Utiles.select_file import  select_file_or_directory

class Load_data:
  def get_name(self):
    return "Load_data"

  def run(self):

      path_jsonl = select_file_or_directory()
      data_response = openai.files.create(
        file=open(path_jsonl, "rb"),
        purpose="fine-tune"
      )
      print(data_response)





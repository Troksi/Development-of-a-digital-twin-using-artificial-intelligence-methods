import openai
import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_dir)

from Utiles.select_file import  select_file_or_directory

class Train_model:
  def get_name(self):
    return "Train_model"

  def run(self):
    training_file = input('training_file: ')
    data_response = client.fine_tuning.jobs.create(
        training_file=training_file, 
        model="gpt-3.5-turbo"
        )
    print(data_response)


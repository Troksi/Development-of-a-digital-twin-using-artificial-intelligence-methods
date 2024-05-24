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


class Train_model:
  openai_key = YOUR_OPENAI_API_KEY

  def __init__(self, openai_key=openai_key):
    self.openai_key = openai_key
    openai.api_key = self.openai_key

  def get_name(self):
    return "Train_model"

  def run(self):
    try:
      training_file = input('training_file: ')
      data_response = openai.FineTuningJob.create(
          training_file=training_file, 
          model="gpt-3.5-turbo"
          )
      fine_tune_logger.info(f'train model with file: {training_file} \n job info: {data_response}')
      print(data_response)
    except Exception as ex:
      fine_tune_logger.error(f'error train with file: {training_file}\n error: {ex}')


if __name__ == "__main__":
  train_model = Train_model()
  train_model.run()

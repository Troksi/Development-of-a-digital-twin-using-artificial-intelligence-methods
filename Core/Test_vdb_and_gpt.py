import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from vbd_manager import VDBManager
from connection import Embedding, get_gpt_answer
from prompt import Prompt
from constants import YOUR_BOT_TOCKEN
from messagehistory import MessageHistory
import vdb

try:
    message_history = MessageHistory(csv_file='Test_vdb_and_gpt.csv')
    VDBManager().run_manager()
    vbd = vdb.VectorStore()
    query = 'почему небо голубое?'

    responses = get_gpt_answer()
    message_history.toNote('gpt' ,responses)
    products_from_vbd = vbd.query(query)
    product = products_from_vbd[0].page_content
    message_history.toNote('vdb1' ,product)
    message_history.toNote('vdb2' ,products_from_vbd[1].page_content)

    responses = get_gpt_answer(f'Дай ответ на вопрос почему небо голубое? Повтори стиль как здесь: {product}')
    message_history.toNote('gpt' ,responses)
except ex:
     message_history.toNote('ERROR: ' ,ex)


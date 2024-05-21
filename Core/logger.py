import logging
import os
from datetime import datetime


current_date = datetime.now().date()

# Get the path to the parent directory of the current script
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Create a directory for log files in the parent directory
log_dir = os.path.join(parent_dir, 'logs')
daily_log_dir = os.path.join(log_dir, str(current_date))
os.makedirs(daily_log_dir, exist_ok=True)

logger_message_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

gpt_logger = logging.getLogger(name='gpt')
gpt_logger.setLevel(logging.NOTSET)
gpt_handler = logging.FileHandler(f'{daily_log_dir}\\gpt.log', 'a', 'utf-8')
gpt_handler.setLevel(logging.NOTSET)
gpt_handler.setFormatter(logger_message_format)
gpt_logger.addHandler(gpt_handler)

gpt_debug_logger = logging.getLogger(name='gpt_debug')
gpt_debug_logger.setLevel(logging.DEBUG)
gpt_debug_handler = logging.FileHandler(f'{daily_log_dir}\\gpt_debug.log', 'a', 'utf-8')
gpt_debug_handler.setLevel(logging.DEBUG)
gpt_debug_handler.setFormatter(logger_message_format)
gpt_debug_logger.addHandler(gpt_debug_handler)

bot_logger = logging.getLogger(name='bot')
bot_logger.setLevel(logging.NOTSET)
bot_handler = logging.FileHandler(f'{daily_log_dir}\\bot.log', 'a', 'utf-8')
bot_handler.setLevel(logging.NOTSET)
bot_handler.setFormatter(logger_message_format)
bot_logger.addHandler(bot_handler)

bot_debug_logger = logging.getLogger(name='bot_debug')
bot_debug_logger.setLevel(logging.DEBUG)
bot_debug_handler = logging.FileHandler(f'{daily_log_dir}\\bot_debug.log', 'a', 'utf-8')
bot_debug_handler.setLevel(logging.DEBUG)
bot_debug_handler.setFormatter(logger_message_format)
bot_debug_logger.addHandler(bot_debug_handler)

vdb_logger = logging.getLogger(name='vdb')
vdb_logger.setLevel(logging.INFO)
vdb_handler = logging.FileHandler(f'{daily_log_dir}\\vdb.log', 'a', 'utf-8')
vdb_handler.setLevel(logging.INFO)
vdb_handler.setFormatter(logger_message_format)
vdb_logger.addHandler(vdb_handler)

vdb_debug_logger = logging.getLogger(name='vdb_debug')
vdb_debug_logger.setLevel(logging.DEBUG)
vdb_debug_handler = logging.FileHandler(f'{daily_log_dir}\\vdb_debug.log', 'a', 'utf-8')
vdb_debug_handler.setLevel(logging.DEBUG)
vdb_debug_handler.setFormatter(logger_message_format)
vdb_debug_logger.addHandler(vdb_debug_handler)

utiles_logger = logging.getLogger(name='utiles')
utiles_logger.setLevel(logging.INFO)
utiles_handler = logging.FileHandler(f'{daily_log_dir}\\utiles.log', 'a', 'utf-8')
utiles_handler.setLevel(logging.INFO)
utiles_handler.setFormatter(logger_message_format)
utiles_logger.addHandler(utiles_handler)
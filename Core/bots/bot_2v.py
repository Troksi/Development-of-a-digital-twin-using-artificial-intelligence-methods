import sys
import os
import telebot

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from connection import Embedding, get_gpt_answer
from prompt import Prompt
from constants import YOUR_BOT_TOCKEN
from logger import bot_logger, bot_debug_logger, gpt_logger, gpt_debug_logger
from messagehistory import MessageHistory
from prompt_split import prompts_split 
from vbd_manager import VDBManager
import vdb

parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_dir)

from Utiles.splitFile import split_text_by_paragraph


class Bot_status(object):
    isStartConversation = False
    actor = Prompt.ACTOR_YariyVagin

    def __init__(self):
        isStartConversation = False

try:
    bot_logger.info('Start work')
    bot_debug_logger.info('Start work')
    gpt_logger.info('Start work')
    gpt_debug_logger.info('Start work')

    bot = telebot.TeleBot(YOUR_BOT_TOCKEN)
    bot_state = Bot_status

    VDBManager().run_manager()    
    vbd = vdb.VectorStore()

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        try:
            responses = ''
            # louding history 
            message_history = MessageHistory(csv_file=f'{message.from_user.username}.csv')

            bot_debug_logger.debug(message.text)
            bot_debug_logger.debug(f'bot_state.isStartConversation: {bot_state.isStartConversation}')
            actor = bot_state.actor

            if not bot_state.isStartConversation and message.text == "/Go":
                bot_state.isStartConversation = True
                bot_logger.info('Start conversation')

                # send start ruls
                responses = get_gpt_answer(Prompt.RULS + actor, role='assistant')
                bot_debug_logger.debug(f'GPT: {responses}')
                bot.send_message(message.from_user.id, responses)
                
                # set answer to history
                message_history.toNote('assistant' ,responses)
            elif bot_state.isStartConversation and message.text == "/Stop":
                bot_state.isStartConversation = False
                message_history.move_to_archive()
                _ = get_gpt_answer('СТОП')
            elif bot_state.isStartConversation:
                 # set question to history
                message_history.toNote( message.from_user.username, message.text)
                # preparing the query
                Prompt.LOOK_QUESTION 
                Prompt.GIVE_ANSWER_LIKE

                prepared_question = Prompt.GIVE_TENTATIVE_ANSWER  + message.text
                query = get_gpt_answer(prepared_question)
                products_from_vbd = vbd.query(query)
                
                bot_debug_logger.debug(f'Bot sistem: {prepared_question}')
                bot_debug_logger.debug(f'GPT: {query}')
                bot_debug_logger.debug(f'VDB: {products_from_vbd[0].page_content}')

                prepared_question = f'{Prompt.LOOK_QUESTION} {message.text} {Prompt.GIVE_ANSWER_LIKE} {products_from_vbd[0].page_content} '
                split_prepared_question = split_text_by_paragraph(prepared_question)
                split_prepared_question_for_hint = prompts_split(split_prepared_question)
                
                for prepared_question in split_prepared_question_for_hint:
                    responses = get_gpt_answer(prepared_question)
                    bot_debug_logger.debug(f'Bot sistem: {prepared_question}')
                    bot_debug_logger.debug(f'GPT: {responses}')
                
                 # set answer to messager
                bot.send_message(message.from_user.id, responses)

                 # set answer to history
                message_history.toNote('assistant' ,responses)
            else:
                bot.send_message(message.from_user.id, "Приветствую! Для начала диалога напиши /Go.\nДля прекращения диалога /Stop")   
        except Exception as e:
            print(e)
            bot_logger.warning(e)


    bot.polling(none_stop=True, interval=0)    
finally:
    bot_logger.info('End work')
    bot_debug_logger.info('End work')
    gpt_logger.info('End work')
    gpt_debug_logger.info('End work')

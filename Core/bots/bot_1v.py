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

class Bot_status(object):
    isStartConversation = False
    actor = Prompt.ACTOR

    def __init__(self):
        isStartConversation = False

try:
    bot_logger.info('Start work')
    bot_debug_logger.info('Start work')
    gpt_logger.info('Start work')
    gpt_debug_logger.info('Start work')

    bot = telebot.TeleBot(YOUR_BOT_TOCKEN)
    bot_state = Bot_status
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        try:
            message_history = MessageHistory(csv_file=f'{message.from_user.username}.csv')

            bot_debug_logger.debug(message.text)
            bot_debug_logger.debug(f'bot_state.isStartConversation: {bot_state.isStartConversation}')
            actor = bot_state.actor
            if not bot_state.isStartConversation and message.text == "/Go":
                bot_state.isStartConversation = True
                bot_logger.info('Start conversation')
                responses = get_gpt_answer(Prompt.RULS + actor)
                bot_debug_logger.debug(f'GPT: {responses}')
                bot.send_message(message.from_user.id, responses)
                message_history.toNote('system' ,responses)
            elif not bot_state.isStartConversation and message.text == "/setActor":
                 bot.register_next_step_handler(message, set_actor)
            elif bot_state.isStartConversation and message.text == "/Stop":
                bot_state.isStartConversation = False
                message_history.move_to_archive()
                _ = get_gpt_answer('СТОП')
            elif bot_state.isStartConversation:
                message_history.toNote( message.from_user.username, message.text)
                responses = get_gpt_answer(message.text)
                bot_debug_logger.debug(f'USER: {message.text}')
                bot_debug_logger.debug(f'GPT: {responses}')
                bot.send_message(message.from_user.id, responses)
                message_history.toNote('system' ,responses)
            else:
                bot.send_message(message.from_user.id, "Приветствую! Для начала диалога напиши /Go.\nДля прекращения диалога /Stop\nДля назначения своего персонажа /setActor")   
        except Exception as e:
            print(e)
            bot_logger.warning(e)
    
    def set_actor(message):
        bot_state.actor = get_gpt_answer(Prompt.SEARCH_ACTOR + message.text)
        bot_debug_logger.debug(f'GPT: {bot_state.actor}')
        bot_debug_logger.info(f'Set actor:{bot_state.actor}')


    bot.polling(none_stop=True, interval=0)    
finally:
    bot_logger.info('End work')
    bot_debug_logger.info('End work')
    gpt_logger.info('End work')
    gpt_debug_logger.info('End work')

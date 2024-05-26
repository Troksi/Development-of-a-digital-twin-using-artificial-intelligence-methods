import sys
import os
import math
import numpy as np
from nltk import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_dir)

from Utiles.t5_02 import get_extracted_texts_from_json

def calculate_perplexity(texts, n):
    # Tokenize the text
    tokenized_text = [list(map(str.lower, word_tokenize(text))) for text in texts]
    
    # Prepare the data for the language model
    train_data, padded_vocab = padded_everygram_pipeline(n, tokenized_text)
    
    # Train the language model
    model = MLE(n)
    model.fit(train_data, padded_vocab)
    
    # Compute perplexity
    perplexity = model.perplexity(tokenized_text)
    return perplexity

# # Example usage
# texts = ["This is a sample sentence for evaluation.", "Another sample sentence."]
# # texts = ["Очень жаль, что вы оказались в такой ситуации.","Противостоять обесцениванию, травле, нереалистичным требованиям или харрасменту бывает непросто. Если помнить, как люди становятся токсичными, станет легче не принимать их поведение на свой счет и абстрагироваться. Токсичное общение — это всегда попытка компенсировать внутреннюю боль, адресуя его другому. Например, у мальчика был жестокий отец, который критиковал его за любую оплошность и наказывал, когда тот пытался защититься, огрызнуться или возразить. Став взрослым, он может разряжать накопленную ярость на сотрудниках как требовательный и неуступчивый руководитель. Понимание, что поведение руководителя — его способ не чувствовать себя маленьким мальчиком в ситуации угрозы, помогает выстроить внутренний барьер между его действиями и собственной психикой. Одновременно очень важно найти способ «разгрузить» вызываемые ситуацией на работе чувства: пожаловаться, рассказать кому-то о том, как устал или злишься. Попробуйте сесть и продумать по шагам: как вы можете организовать себе поддержку прямо сейчас? Стратегия, которую можно применять в рабочих отношениях, чтобы снизить градус напряжения – «кофейный автомат». Вы взаимодействуете с коллегами, как при покупке кофе: выбираете напиток – вносите деньги – забираете чашку. То есть, максимально технично и сухо, избегая эмоционального взаимодействия, ограничивая контакт действиями в рамках ваших должностных обязанностей. Важный момент: вы говорите, что вашего опыта недостаточно, чтобы перейти на другую работу. Это может быть когнитивной ошибкой, и место, где вы работаете, отнюдь не единственное, куда можно устроиться. Возможно, дело не в объективном недостатке опыта, а неуверенности в собственных силах, «синдроме самозванца», завышенных представлениях о качествах, которыми обладает хороший сотрудник. Поэтому в любом случае составьте план эвакуации: что нужно сделать, чтобы уволиться? Разбейте этот план на этапы и конкретные сроки. Его не обязательно применять, но он может стать «ремнем безопасности», который выручит, если ситуация станет критической."]

# # json_path = 'extracted_texts.json'
# # texts = get_extracted_texts_from_json(json_path)
# n = 3
# perplexity = calculate_perplexity(texts, n)
# print(f"Perplexity: {perplexity}")

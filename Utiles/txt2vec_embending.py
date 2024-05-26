import openai
import os
import sys
import numpy as np
import json

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from Core.constants import YOUR_OPENAI_API_KEY
from Utiles.pause4limit import PauseForLimit


def update_json_file(input_file_path, output_file_path, fild):
    # Загружаем исходный JSON файл
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Если выходной файл уже существует, считываем его содержимое
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = []
    
    pauseForLimit = PauseForLimit(2, 61)
    # Обрабатываем данные и обновляем их
    # Открываем выходной файл в режиме записи (overwrite) для инициализации списка
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

    # Обрабатываем данные и обновляем их
    with open(output_file_path, 'a', encoding='utf-8') as f:
        for item in data:
            pauseForLimit.reg_stap()
            processed_value = get_embedding(item[fild])
            updated_item = {
                "request": item["request"],
                "ref": processed_value #item["trm"]
            }
            f.write(json.dumps(updated_item, ensure_ascii=False, indent=4) + '\n')


def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model).data[0].embedding

def calculate_cosine_simelar(vec_a, vec_b):

    dot_prod = np.dot(vec_a, vec_b)

    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    cos_similarity = dot_prod / (norm_a * norm_b)
    
    return cos_similarity

if __name__ == "__main__":

    openai.api_key = YOUR_OPENAI_API_KEY

    
    # Пример использования
    input_file_path = r'Utiles\telegram_messages_OkYasno\Datas\mv_result.json'
    output_file_path =  r'Utiles\telegram_messages_OkYasno\Datas\mv_result_embanding_ref.json'
    fild = 'ref'
    update_json_file(input_file_path, output_file_path, fild)

    # embedded_vec_1 = np.array(get_embedding("Text1"))
    # embedded_vec_2 = np.array(get_embedding("Text1"))

    # similarity_score = calculate_cosine_simelar(embedded_vec_1,embedded_vec_2)

    # print(similarity_score)

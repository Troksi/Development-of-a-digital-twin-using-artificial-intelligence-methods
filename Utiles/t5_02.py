import os
import json

def get_extracted_texts_from_json(json_path):
    extracted_texts = []
    
    # Проверяем, существует ли файл
    if not os.path.exists(json_path):
        print(f"File {json_path} does not exist.")
        return extracted_texts
    
    # Открываем и читаем JSON-файл
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        # Проверяем структуру данных и извлекаем текст
        for item in data:
            if 'extracted_text' in item:
                extracted_texts.append(item['extracted_text'])
    
    return extracted_texts

# Пример использования
# json_path = r'telegram_messages_polit_girik\_Отвечает Политический Алгоритм ИИ «Жириновский»_/extracted_texts.json'
# extracted_texts = get_extracted_texts_from_json(json_path)
# print(extracted_texts)

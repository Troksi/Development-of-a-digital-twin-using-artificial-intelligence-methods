import os
import json
import re

def extract_texts_from_files(directory_path):
    results = []
    pattern = re.compile(r', ЛДПР: -(.*)', re.DOTALL)
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = pattern.search(content)
                    if match:
                        extracted_text = match.group(1).strip()
                        results.append({
                            "file": file,
                            "extracted_text": extracted_text
                        })
    
    # Сохранение результатов в JSON
    output_path = os.path.join(directory_path, 'extracted_texts.json')
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)
    
    print(f'Extracted texts saved to {output_path}')

# Пример использования
directory_path = r'telegram_messages_polit_girik\_Отвечает Политический Алгоритм ИИ «Жириновский»_'
extract_texts_from_files(directory_path)

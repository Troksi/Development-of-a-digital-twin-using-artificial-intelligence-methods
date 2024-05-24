import os
import re

def extract_names_from_files(directory):
    names = []
    pattern = re.compile(r'✔️Отвечает\s+(\w+\s\w+)')

    # Проверяем, существует ли указанный каталог
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return names

    # Проходим по всем файлам в указанном каталоге
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Ищем все совпадения в содержимом файла
                found_names = pattern.findall(content)
                names.extend(found_names)
            except Exception as e:
                print(f"Failed to process file: {file_path} due to {e}")

    return names

# Пример использования функции
directory = 'telegram_messages_OkYasno'
extracted_names = extract_names_from_files(directory)
print(f"Extracted names: {extracted_names}")
print(f"Extracted names: {len(extracted_names)}")
print(f"Extracted names: {len(set(extracted_names))}")

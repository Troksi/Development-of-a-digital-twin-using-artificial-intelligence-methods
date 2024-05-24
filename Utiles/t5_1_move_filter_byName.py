import os
import re
import shutil

def move_files_to_named_directories(directory):
    # Регулярное выражение для поиска имен
    pattern = re.compile(r'✔️Отвечает\s+(\w+\s\w+)')

    # Проверяем, существует ли указанный каталог
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return

    # Проходим по всем файлам в указанном каталоге
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Ищем имя в содержимом файла
                match = pattern.search(content)
                if match:
                    name = match.group(1)
                    name_directory = os.path.join(directory, name)

                    # Создаем каталог, если он не существует
                    if not os.path.exists(name_directory):
                        os.makedirs(name_directory)

                    # Перемещаем файл в соответствующий каталог
                    shutil.move(file_path, os.path.join(name_directory, filename))
                    print(f'Moved file {filename} to {name_directory}')
                else:
                    print(f'No name found in file {filename}')
            except Exception as e:
                print(f"Failed to process file: {file_path} due to {e}")

# Пример использования функции
directory = 'telegram_messages_OkYasno'
move_files_to_named_directories(directory)

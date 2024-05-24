import os

def remove_first_line_from_txt_files(directory):
    # Проверяем, существует ли указанный каталог
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return

    # Проходим по всем файлам в указанном каталоге
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Проверяем, является ли текущий элемент текстовым файлом с расширением .txt
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            try:
                # Читаем содержимое файла
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Если файл не пустой, удаляем первую строку и записываем обратно
                if lines:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.writelines(lines[1:])
                    print(f"Processed file: {file_path}")
                else:
                    print(f"File is empty: {file_path}")
            except Exception as e:
                print(f"Failed to process file: {file_path} due to {e}")

# Пример использования функции
directory = 'telegram_messages_OkYasno'
remove_first_line_from_txt_files(directory)

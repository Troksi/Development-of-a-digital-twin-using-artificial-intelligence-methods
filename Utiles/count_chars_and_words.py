import os
import re

def count_chars_and_words(file_path):
    # Инициализируем переменные для подсчета символов и слов
    total_chars = 0
    total_words = 0
    
    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем содержимое файла
            content = file.read()
            
            # Считаем символы
            total_chars += len(content)
            
            # Используем регулярное выражение для подсчета слов
            words = re.findall(r'\b\w+\b', content)
            total_words += len(words)
            
            print(f"Файл: {file_path}")
            print(f"Количество символов: {total_chars}")
            print(f"Количество слов: {total_words}")
            print()
            
            return total_chars, total_words
        
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {str(e)}")
        return 0, 0

def process_text_files(directory):
    total_chars = 0
    total_words = 0
    
    # Проверяем, что указанный путь существует и является директорией
    if not os.path.isdir(directory):
        print("Указанный путь не является директорией.")
        return
    
    # Получаем список всех файлов в указанной директории
    file_list = os.listdir(directory)
    
    # Фильтруем список файлов, оставляя только файлы с расширением .txt
    txt_files = [file for file in file_list if file.endswith('.txt')]
    
    if not txt_files:
        print("В указанной директории нет файлов с расширением .txt.")
        return
    
    # Обрабатываем каждый txt файл, вызывая функцию count_chars_and_words
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        chars, words = count_chars_and_words(file_path)
        total_chars += chars
        total_words += words
    
    print("Общее количество символов:", total_chars)
    print("Общее количество слов:", total_words)

# Пример использования
directory_path = input("Введите путь к директории: ")
process_text_files(directory_path)

# import os
# import re

# def count_chars_and_words(file_path):
#     # Инициализируем переменные для подсчета символов и слов
#     total_chars = 0
#     total_words = 0
    
#     try:
#         # Открываем файл для чтения
#         with open(file_path, 'r', encoding='utf-8') as file:
#             # Читаем содержимое файла
#             content = file.read()
            
#             # Считаем символы
#             total_chars += len(content)
            
#             # Используем регулярное выражение для подсчета слов
#             words = re.findall(r'\b\w+\b', content)
#             total_words += len(words)
            
#             return total_chars, total_words
        
#     except Exception as e:
#         print(f"Ошибка при обработке файла {file_path}: {str(e)}")
#         return 0, 0

# def process_text_files(directory):
#     total_chars = 0
#     total_words = 0
#     num_files = 0
    
#     # Проверяем, что указанный путь существует и является директорией
#     if not os.path.isdir(directory):
#         print("Указанный путь не является директорией.")
#         return
    
#     # Получаем список всех файлов в указанной директории
#     file_list = os.listdir(directory)
    
#     # Фильтруем список файлов, оставляя только файлы с расширением .txt
#     txt_files = [file for file in file_list if file.endswith('.txt')]
    
#     if not txt_files:
#         print("В указанной директории нет файлов с расширением .txt.")
#         return
    
#     # Обрабатываем каждый txt файл, вызывая функцию count_chars_and_words
#     for txt_file in txt_files:
#         file_path = os.path.join(directory, txt_file)
#         chars, words = count_chars_and_words(file_path)
#         total_chars += chars
#         total_words += words
#         num_files += 1
    
#     # Подсчет среднего количества символов и слов
#     if num_files > 0:
#         avg_chars = total_chars / num_files
#         avg_words = total_words / num_files
#     else:
#         avg_chars = 0
#         avg_words = 0
    
#     print("Общее количество символов:", total_chars)
#     print("Общее количество слов:", total_words)
#     print("Среднее количество символов в файле:", avg_chars)
#     print("Среднее количество слов в файле:", avg_words)

# # Пример использования
# directory_path = input("Введите путь к директории: ")
# process_text_files(directory_path)

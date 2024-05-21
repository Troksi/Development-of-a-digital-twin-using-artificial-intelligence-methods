import os
import sys


current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from logger import utiles_logger


def display(message: str) -> None:
    print(message)
    utiles_logger.info(f"splitFile: {message}")


def split_text_by_symboles(content):
    return [content[i:i+1500] for i in range(0, len(content), 1500)]


def split_text_by_paragraph(text, max_len_txt=1400) -> list[str]:
    if len(text) <= max_len_txt:
        return [text]
    else:
        paragraphs = text.split('.')
        paragraphs = [s for s in paragraphs if s.strip()]
        result = []
        temp_text = ''
        for paragraph in paragraphs:
            if len(temp_text) + len(paragraph) + 1 <= max_len_txt:
                temp_text += paragraph + '.'
            else:
                result.append(temp_text)
                temp_text = paragraph + '.'

        if temp_text:
            result.append(temp_text)

        return result


def split_text_file(txt_path: str) -> None:
    # Проверяем, существует ли файл
    if not os.path.exists(txt_path):
        display("Файл не найден.")
        return

    # Читаем содержимое файла
    with open(txt_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Проверяем, превышает ли количество символов в файле пороговое значение
    if len(content) <= 1500:
        display(
            "Количество символов в файле не превышает 1500. Разделение не требуется.")
        return

    display(f"Количество символов:{len(content)}")
    # Разделяем текст на части
    chunks = split_text_by_paragraph(content)
    # Создаем и сохраняем разделенные файлы
    for i, chunk in enumerate(chunks):
        new_file_path = f"{os.path.splitext(txt_path)[0]}_{i+1}{os.path.splitext(txt_path)[1]}"
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(chunk)

        display(f"Создан файл: {new_file_path}")


# # Пример использования:
# txt_file_path = "lomonosov_perepiska_mod.txt"  # Путь к вашему файлу TXT
# split_text_file(txt_file_path)

def process_txt_files(directory: str) -> None:
    # Проверяем, что указанный путь существует и является директорией
    if not os.path.isdir(directory):
        display("Указанный путь не является директорией.")
        return

    # Получаем список всех файлов в указанной директории
    file_list = os.listdir(directory)
    # Фильтруем список файлов, оставляя только файлы с расширением .txt
    txt_files = [file for file in file_list if file.endswith('.txt')]
    if not txt_files:
        display("В указанной директории нет файлов с расширением .txt.")
        return

    display("Найденые файлы:")
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        display(f"{file_path}")

    display(f"Количество файлов: {len(txt_files)}")
    request = input("Продолжить? Y/N ")
    if request in ['n', 'N']:
        display("Exit")
        return

    # Обрабатываем каждый txt файл, вызывая функцию split_txt
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        display(f"Обработка файла: {file_path}")
        split_text_file(file_path)

if __name__=="__main__":
    # Пример использования
    directory_path = input("Введите путь к директории: ")
    process_txt_files(directory_path)

import os
import csv
from datetime import datetime
import shutil
import zipfile

class MessageHistory:
    def __init__(self, folder='messages', csv_file='message_history.csv'):
        current_dir = os.path.dirname(__file__)
        folder_dir = os.path.join(folder, csv_file)
        self.csv_file_name = csv_file
        self.csv_file = os.path.join(current_dir, folder_dir)
        self.history = []

    def toNote(self, author, message):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, author, message])
    
    def takeOffHistory(self):
        with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.history.append({'time':row[0], 'author': row[1], 'message': row[2]})
        return self.history
    
    
    def takeOffHistory_for_api(self):
        with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.history.append({'role': row[1], 'content': row[2]})
        return self.history

    def move_to_archive(self):
        file_name = self.csv_file_name
        file_path = self.csv_file
        # Путь к текущему каталогу
        current_directory = os.getcwd()

        # Путь к архиву
        archive_path = os.path.join(current_directory, 'archive.zip')

        # Если архива нет, создаем его
        if not os.path.exists(archive_path):
            with zipfile.ZipFile(archive_path, 'w') as archive:
                pass  # Создаем пустой архив

        # Генерируем уникальное имя для файла
        unique_file_name = generate_unique_name(file_name)

        # Перемещаем файл в архив
        try:
            with zipfile.ZipFile(archive_path, 'a') as archive:
                archive.write(file_path, unique_file_name)
            os.remove(file_path)  # Удаляем оригинальный файл после перемещения
            print(f"Файл '{file_name}' успешно перемещен в архив с именем '{unique_file_name}'.")
        except Exception as e:
            print(f"Произошла ошибка при перемещении файла в архив: {e}")

def generate_unique_name(file_name):
    # Разделитель для добавления временной метки
    separator = '_'
    # Получаем текущую дату и время
    current_time = datetime.now()
    # Генерируем уникальное имя файла с временной меткой
    unique_name = f"{os.path.splitext(file_name)[0]}_{current_time.strftime('%Y%m%d%H%M%S')}{os.path.splitext(file_name)[1]}"
    return unique_name



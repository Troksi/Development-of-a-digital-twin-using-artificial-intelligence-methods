import os
import json

def collect_file_statistics(base_directory, output_json):
    # Проверяем, существует ли указанный каталог
    if not os.path.isdir(base_directory):
        print(f"Directory does not exist: {base_directory}")
        return
    
    statistics = {}

    # Проходим по всем подкаталогам в базовом каталоге
    for subdir in os.listdir(base_directory):
        subdir_path = os.path.join(base_directory, subdir)
        if os.path.isdir(subdir_path):
            file_count = 0
            # Считаем количество файлов в подкаталоге
            for _, _, files in os.walk(subdir_path):
                file_count += len(files)
            statistics[subdir] = file_count

    # Сохраняем статистику в JSON файл
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(statistics, json_file, indent=4, ensure_ascii=False)
    
    print(f"Statistics saved to {output_json}")

# Пример использования функции
base_directory = 'telegram_messages_OkYasno/Психологи'
output_json = 'telegram_messages_OkYasno/Психологи/statistics.json'
collect_file_statistics(base_directory, output_json)

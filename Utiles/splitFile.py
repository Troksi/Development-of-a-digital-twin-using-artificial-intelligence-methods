import os

def split_text_file(txt_path):
    # Проверяем, существует ли файл
    if not os.path.exists(txt_path):
        print("Файл не найден.")
        return

    # Читаем содержимое файла
    with open(txt_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Проверяем, превышает ли количество символов в файле пороговое значение
    if len(content) <= 150000:
        print("Количество символов в файле не превышает 150000. Разделение не требуется.")
        return
    
    print(f"Количество символов:{len(content)}")

    # Разделяем текст на части
    chunks = [content[i:i+150000] for i in range(0, len(content), 150000)]

    # Создаем и сохраняем разделенные файлы
    for i, chunk in enumerate(chunks):
        new_file_path = f"{os.path.splitext(txt_path)[0]}_{i+1}{os.path.splitext(txt_path)[1]}"
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(chunk)
        print(f"Создан файл: {new_file_path}")

# Пример использования:
txt_file_path = "lomonosov_perepiska_mod.txt"  # Путь к вашему файлу TXT
split_text_file(txt_file_path)

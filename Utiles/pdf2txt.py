import fitz

def pdf_to_text(pdf_path, txt_path) -> None:
    # Открываем PDF файл
    document = fitz.open(pdf_path)

    text = ""
    # Проходим по всем страницам PDF и извлекаем текст
    for page_number in range(document.page_count):
        page = document.load_page(page_number)
        text += page.get_text()

    # Закрываем PDF файл
    document.close()

    # Сохраняем текст в файл TXT
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    print(f"Текст из PDF файла сохранен в {txt_path}")

# Пример использования:
pdf_file_path = "lomonosov_perepiska_1737-1765_2011.pdf"  # Путь к вашему PDF файлу
txt_file_path = "output.txt"    # Путь для сохранения файла TXT
pdf_to_text(pdf_file_path, txt_file_path)

import os
import pdfplumber

def extract_pages_to_txt(pdf_path: str, page_ranges: List[Tuple[int, int]], output_dir: str) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with pdfplumber.open(pdf_path) as pdf:
        for start_page, end_page in page_ranges:
            if start_page <= 0 or end_page > len(pdf.pages) or start_page > end_page:
                print(f"Ошибка: Некорректный диапазон страниц: {start_page}-{end_page}")
                continue

            text = ""
            for page_num in range(start_page - 1, end_page):
                page = pdf.pages[page_num]
                text += page.extract_text()

            output_file_path = os.path.join(output_dir, f"pages_{start_page}-{end_page}.txt")
            with open(output_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)

            print(f"Страницы {start_page}-{end_page} успешно записаны в файл: {output_file_path}")

# Пример использования функции
pdf_path = "lomonosov_perepiska_1737-1765_2011.pdf"
output_directory = "extracted_text"  # Папка для сохранения текстовых файлов

# page_ranges_to_extract = [
#     (17, 20),
#     (24, 25),
#     (29, 32),
#     (35, 39),
#     (40, 51),
#     (58, 65),
#     (66, 69),
#     (70, 74)
#     ]
page_ranges_to_extract = [
    (77, 78),
    (80, 99),
    (102, 107),
    (108, 111),
    (121, 127),
    (128, 131),
    (132, 133),
    (138, 139),
    (144, 145),
    (146, 147),
    (147, 149),
    (149, 152),
    (162, 165),
    (166, 169),
    (170, 172),
    (173, 175)
    ]
extract_pages_to_txt(pdf_path, page_ranges_to_extract, output_directory)
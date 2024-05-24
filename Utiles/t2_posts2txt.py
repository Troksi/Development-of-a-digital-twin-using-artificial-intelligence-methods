import os
import json

def clean_text(text):
    """
    Удаляет лишние пробелы и переносы строк из текста.
    """
    return ' '.join(text.split())

def save_messages_to_txt(file_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the processed JSON data
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Process each message and save to a text file
    for message in data.get('messages', []):
        message_id = message.get('id')
        date = message.get('date')
        text = message.get('text')
        
        if message_id is not None:
            clean_text_content = clean_text(text)
            # Skip saving if the text is empty after cleaning
            if not clean_text_content:
                continue
            
            file_name = f"id_{message_id}.txt"
            file_path = os.path.join(output_dir, file_name)
            
            with open(file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(f"{date}\n{clean_text_content}")

# Example usage
input_file = 'processed_result_OkYasno.json'
output_directory = 'telegram_messages_OkYasno'

save_messages_to_txt(input_file, output_directory)

import os
import shutil

def find_and_move_files_by_length(directory, max_length):
    # Create the target directory inside the specified directory if it doesn't exist
    target_directory = os.path.join(directory, f"_{max_length}_")
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Only process text files
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Check if the length of the text is less than the specified maximum length
            if len(content) < max_length:
                # Ensure the file is closed before moving
                shutil.move(file_path, os.path.join(target_directory, filename))

# Example usage
input_directory = 'telegram_messages'
max_length = int(input('Длина текста: '))

find_and_move_files_by_length(input_directory, max_length)

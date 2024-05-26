import os
import shutil

def find_and_move_files_by_length(directory, max_length):
    target_directory = os.path.join(directory, f"_{max_length}_")
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if len(content) < max_length:
                shutil.move(file_path, os.path.join(target_directory, filename))

# Example usage
input_directory = 'path\to\directory'
max_length = int(input('Длина текста: '))
find_and_move_files_by_length(input_directory, max_length)
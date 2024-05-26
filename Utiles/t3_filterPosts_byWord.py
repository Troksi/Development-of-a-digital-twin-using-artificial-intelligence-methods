import os
import shutil

def find_and_move_files(directory, keyword):
    
    target_directory = os.path.join(directory, f"_{keyword}_")
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if keyword in content:
                shutil.move(file_path, os.path.join(target_directory, filename))

# Example usage
input_directory = 'path\to\directory'
search_keyword = input('Слово для поиска: ')
find_and_move_files(input_directory, search_keyword)

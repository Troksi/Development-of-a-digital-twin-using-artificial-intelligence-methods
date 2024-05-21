import os


def select_file_or_directory(start_path='.'):
    current_path = os.path.abspath(start_path)

    while True:
        print(f"\nCurrent directory: {current_path}")
        items = os.listdir(current_path)
        items.insert(0, '..')  # Опция для выхода в родительский каталог

        for idx, item in enumerate(items):
            print(f"{idx}. {item}")

        choice = input("Enter the number of the item to select (or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting selection.")
            break

        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(items):
                selected_item = items[choice]
                selected_path = os.path.join(current_path, selected_item)

                if os.path.isdir(selected_path):
                    current_path = selected_path
                else:
                    print(f"You selected the file: {selected_path}")
                    return selected_path
            else:
                print("Invalid choice, please try again.")
        else:
            print("Invalid input, please try again.")

# # Пример использования функции
# selected_path = select_file_or_directory()
# print(f"Selected path: {selected_path}")
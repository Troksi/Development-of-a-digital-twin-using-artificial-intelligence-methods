from load_data import Load_data
from train_model import Train_model

class MenuItem:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        return self.name

    def execute(self):
        self.action()

class Menu:
    def __init__(self):
        self.items = []

    def register_item(self, item):
        item_number = len(self.items) + 1
        self.items.append((item_number, item))

    def display_menu(self):
        for number, item in self.items:
            print(f"{number}. {item}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter the number of the action to perform (or 'q' to quit): ")
            if choice.lower() == 'q':
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.items):
                    _, item = self.items[choice - 1]
                    item.execute()
                else:
                    print("Invalid choice, try again.")
            else:
                print("Invalid input, try again.")

# # Пример классов с методами имени и запуска
# class ExampleClass1:
#     def get_name(self):
#         return "Action 1"

#     def run(self):
#         print("Running Action 1...")

# class ExampleClass2:
#     def get_name(self):
#         return "Action 2"

#     def run(self):
#         print("Running Action 2...")

# # Создаем экземпляры классов
# example1 = ExampleClass1()
# example2 = ExampleClass2()

# # Создаем экземпляры элементов меню
# item1 = MenuItem(example1.get_name(), example1.run)
# item2 = MenuItem(example2.get_name(), example2.run)

load_data = Load_data()
train_model = Train_model()

item_load_data = MenuItem(load_data.get_name(), load_data.run)
item_train_model = MenuItem(train_model.get_name(), train_model.run)

# Создаем меню и регистрируем элементы
menu = Menu()
menu.register_item(item_load_data)
menu.register_item(item_train_model)

# Запускаем меню
menu.run()



# if __name__ == '__main__':
#     state = 1
#     while state != 0:
#         print()
#         state = int(input('Выбирите действие: '))

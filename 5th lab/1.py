import os


choice = input("Вы хотите ввести свою директорию: [Y]-Да [N]-Нет\n  > ")

if choice == 'Y':
    print(len(os.listdir(input("Введите директорию: "))))
else:
    print(len(os.listdir("C:\\Users\Shteyd\Downloads")))
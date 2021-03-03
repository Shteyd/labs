import re

user_str = input("Введите строку: ")
print("Символов:", len(user_str), "\nСлов:", len(re.findall(r"\w+", user_str)))
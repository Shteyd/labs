import re

yourChoice = input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): ")
user_len = input()
some_dict = {
    '1': ' '.join(re.findall(r'\b\w{1,5}\b', user_len)),
    '2': ' '.join(re.findall(r"Ли\w+", user_len)),
    '3': ' '.join(re.findall(r"\w{5,10}", user_len)),
    '4': ' '.join(re.findall(r"\w+ов\b", user_len))
}

print(some_dict[yourChoice])
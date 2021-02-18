import string

yourString = input("Введите строку: "); newString = yourString
for i in list(yourString):
    if i in string.punctuation:
        newString = newString.replace(i, '')

print("Символов:", len(yourString), "\nСлов:", len(newString.split()))
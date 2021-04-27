import re

def adding(message):
    if re.search(r'[a-zA-Z]*\;[а-яА-Я]', message):
        with open("dictionary.csv", "a", encoding = "utf-8") as file:
            file.write(message + "\n")
            return "Вы прекрасны! \nСпасибо!"
    else:
        return "Неверный формат. \nПерепроверьте и попробуйте снова."
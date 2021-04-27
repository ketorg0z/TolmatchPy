import csv, codecs, re

def main(slovo):
    slovar = otkr_csv("dictionary.csv")
    return function(slovo, slovar).upper()


def otkr_csv(file_csv):  # открытие файла csv
    slovar = codecs.open(file_csv, 'r',
                         encoding='utf-8-sig')  # такая кодировка, просто потому что так сложилось, что в ней удобней
    slovar = csv.DictReader(slovar, delimiter=';')
    return slovar


def function(slovo, slovar):
    per = ""
    for slovzo in slovar:
        pattern = '[а-яА-Я]*\)'
        p = re.sub(pattern, '', slovzo['WORD2'])
        if len(p.lower().split()) > 0:
            if slovo.lower() == p.lower().split()[0]:
                per += slovzo['WORD1'].lower() + ', '

    if per == "":
        return "--"
    else:
        return per[0:len(per)-2]
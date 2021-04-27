import csv, codecs, re

def main(slovo):
    slovar = otkr_csv("dictionary.csv")
    slovar2 = otkr_csv("Словарь Ожегов.csv")
    slovo2 = function(slovo, slovar)
    return slovo2.upper().replace('=', '')\
        .replace('>', '').replace('<', '') +"\n"+ function(slovo2, slovar2).replace('=', '')\
        .replace('>', '').replace('<', '')


def otkr_csv(file_csv):  # открытие файла csv
    slovar = codecs.open(file_csv, 'r',
                         encoding='utf-8-sig')
    slovar = csv.DictReader(slovar, delimiter=';')
    return slovar


def function(slovo, slovar):
    per = ""
    for slovzo in slovar:
        if len(slovzo['WORD1'].split()) > 0:
            if slovo.lower().split()[0] == slovzo['WORD1'].lower().split()[0]:
                pattern = '\([а-яА-Я *,-]*\)'
                p = re.sub(pattern, '', slovzo['WORD2'].lower())
                pattern = '[а-яА-Я]*\)'
                per += re.sub(pattern, '', p) + '\n'
    if per == "":
        return "--"
    else:
        return per
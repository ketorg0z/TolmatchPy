from random import randint
import re

def openCSVAsDICT(filename):
    d = {}
    try:
        dictionary = open(filename, 'r', encoding='utf-8').read().split('\n')
        for row in dictionary:
            key, value = row.split(';')
            d[key] = value
    except Exception as err:
        print('Exception' + str(err))
    return d


def getRandPair(d):
    keys = []
    for key in d.keys():
        keys.append(key)
    buff = {}
    pIndex = randint(1, len(keys) - 1)
    buff['question'] = keys[pIndex]
    buff['answer'] = d[keys[pIndex]]
    buff['wrong'] = d[keys[randint(1, len(keys) - 1)]]
    return buff


def main():
    dictionary = openCSVAsDICT('dictionary.csv')
    randPair = getRandPair(dictionary)
    ans_wr = randPair['wrong']
    pattern = '\([а-яА-Я *,-]*\)'
    pattern1 = '[а-яА-Я]*\)'
    wrong_answer = re.sub(pattern, '', ans_wr)
    wrong_answer = re.sub(pattern1, '', wrong_answer)
    ans_cor = randPair['answer']
    correct_answer = re.sub(pattern, '', ans_cor)
    correct_answer = re.sub(pattern1, '', correct_answer)
    return 'What is' + '\t' + randPair['question'] + '?', correct_answer, wrong_answer
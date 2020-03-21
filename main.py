#Developer - Boris Kuznetsov - 100%

import random
import string

zaglav = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ'
def main():
    text = ''
    # file_name = input('Введите имя файла - ')
    try:
        file_name = input('Введите имя файла')

        with open(file_name) as f1:
            for line in f1:
                if line == '\n':
                    continue
                text += line
        replace_end(text)
    except FileNotFoundError:
        print('Нет такого файла, попробуйте еще раз')
        main()


def replace_end(text):
    #text = text.replace('\n', ' \n').replace('.', ' ').replace('; ', ';').replace('—', '').split(' ')
    text = text.replace('\n', ' \n').split(' ')
    # print(text)
    dict_count(text)
    pairs(text)


def pairs(text):
    z = []
    for i in range(len(text)):
        x = []
        if i == (len(text) - 1):
            continue
        elif i != (len(text) - 1):
            x.append(text[i])
            x.append(text[i + 1])
            z.append(x)
    count_pairs(z)


def count_pairs(pairs):
    z = {}
    for pipi in range(len(pairs)):
        q = []
        for i in range(len(pairs)):
            if pairs[i][0] == pairs[pipi][0]:
                q.append(pairs[i][1])
        z[pairs[pipi][0]] = q
    #print(z)
    n = int(input(f'Сколько слов сгенерировать? - '))
    return start_word(z, n)

def start_word(dicts, n):
    rrr = dicts
    try:
        #start = random.choice(list(dicts.keys()))
        start = random.choice(zglav(rrr))
        itog = ''
        q = n
        rec(dicts, start,  q, itog)
    except TypeError:
        return start_word(dicts, n)

def zglav(dicts):
    lii = []
    for i in list(dicts.keys()):
        if i[0] in zaglav:
            lii.append(i)
        else:
            continue
    return lii



def rec(dicts, start, n, itog):
    if n == 0:
        print(itog)
    else:
        try:
            z = random.choice(dicts[start])
            q = random.choice(dicts[z])
            itog+= str(z)+' '+str(q)+' '
            start = q
            return rec(dicts, start, n-1, itog)
        except KeyError:
            return start_word(dicts)

def dict_count(text):
    z = {}
    for i in text:
        z[i] = text.count(i)
    #print(z)


main()

try :
    print(5/0)
except ZeroDivisionError:
    print('Yoy can not divide for zero')
    #print('Привет Алина')
#info = input('Enter text:')
#print(info)

def calc (argOne,argTwo):
    rezult=argOne/argTwo
    return rezult

while True:
    numerator=input('Enter numerate:')
    if numerator== 'q':
        break
    else:
        numerator=float(numerator)
    denominator=input('Enter dinominator')
    if denominator == 'q':
        break
    else:
        denominator = float(denominator)
    try:

        rez = calc(numerator, denominator)

    except ZeroDivisionError:
        print('You can not divide for zero')
        #denominator = int(input('Enter dinominator'))
    else:
        print(rez)

file_name='Alice.py'
try:
    with open(file_name) as f_obj:
        book=f_obj.read()
except FileNotFoundError:
    print('This file not found')


title = 'Alice in Wonderland'
title=title.split()
print(title)

import io
file_name='Alice.txt'

try:
    with io.open(file_name,encoding='utf-8') as f_obj:
        contens=f_obj.read()
except FileNotFoundError:
    msg='Soryy the file {} not found'.format(file_name)
    print(msg)
#except UnicodeDecodeError:
    #print('Erro')

else:
    words=contens.split()
    print(len(words))

# print count words with three book
import word_count
word_count.count_words('Alice.txt','magic.txt','book.txt','little princesse.txt')
word_count.count_word_pass('Alice.txt','magic.txt','book.txt', 'book_two.txt','little princesse.txt')

# -*- coding: utf-8 -*-

#Введите с клавиатуры список с различными значениями (цифры, слова, символы).
# Необходимо проверить, есть ли в этом списке два слова подряд и вывести их на экран.
# Если таких пар нет, то выведите фразу “Мало слов!”.

def solution():
    n = input().split()
    found_pair = False

    if len(n) < 2:
        print('Мало слов')
    else:
        for i in range(len(n) - 1):
            if n[i].isalpha() and n[i + 1].isalpha():
                print(n[i], n[i + 1])
                found_pair = True

        if not found_pair:
            print('Мало слов!')

solution()


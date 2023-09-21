#dodo дописать функцию самой игры

import argparse
import random


def read(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return random.choice([i.strip().lower() for i in f if i.strip()])
    except FileNotFoundError:
        print('Нет такого файла')
        exit()
    except PermissionError:
        print('Отказано в чтении файла')
        exit()
    except:
        print('неизвестная ошибка')
        exit()


def game(file, errors=5):
    word = read(file)
    err = 0
    v = ['*' for i in word]


    print('*' * len(word))

    while err < errors:
        print(f'ошибок {err} из {errors}')
        book = input('введите букву. (0 - все слово) ---> ')
        if book == '0':
            answer = input('введите слово: ').lower().strip()
            if answer == word:
                print(f'вы выиграли! Слово {word}')
                v = list(word)
                break
            else:
                break
        elif book in word and len(book) == 1:
            word_l = [i for i in word]
            for i in range(len(word_l)):
                if book == word_l[i]:
                    v[i] = word_l[i]
            if word_l == v:
                print(f'вы выиграли! Слово {word}')
                break
        else:
            err += 1
            print('такой буквы нет в слове.')
        print(''.join(v))
    if '*' in v:
        print(f"Вы проиграли! Слово {word}")


def parsing():
    parser = argparse.ArgumentParser(
        prog='Виселица',
        description='Угадай слово по букве, с количеством попыток.',
        epilog='Анастасия Тучина 2023'
    )
    parser.add_argument('-e', '--errors', default=5, nargs='?', help='количество ошибок')
    parser.add_argument('-f', '--file', required=True, help="Файл со словами. По одному в строке")

    return parser.parse_args()


if __name__ == '__main__':
    args = parsing()
    game(file=args.file, errors=args.errors)

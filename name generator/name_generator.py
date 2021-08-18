import sys
import random

def load_file(filename):
    try:
        with open(filename) as f:
            load_txt = f.read()
            load_txt = [x.strip().capitalize() for x in load_txt.split('\n')]
            return load_txt
    except:
        sys.exit(0)

load_first_name = load_file('first-name.txt')
load_last_name = load_file('last-name.txt')

while True:
    first_name = random.choice(load_first_name)
    last_name = random.choice(load_last_name)

    print('==========================')
    print(f'{first_name} {last_name}')
    print('===========================')
    print('Generate another? [y/n]')
    print('\n')
    print('\n')

    try_again = input()

    if try_again == 'n':
        break
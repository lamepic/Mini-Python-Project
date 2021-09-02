import sys

def load(file):
    """Loads a text file as a list"""
    try:
        with open(file) as f:
            txt = f.read().strip().split('\n')
            txt = [word.lower() for word in txt]
            return txt
    except IOError:
        print('Error opening file')
        sys.exit(1)

word_list = set(load('2of12.txt'))

palingrams = []

for word in word_list:
    end = len(word)
    reverse = word[::-1]

    if end > 1:
        for i in range(end):
            if word[i:] == reverse[:end-i] and reverse[end-i:] in word_list:
                palingrams.append((word, reverse[end-i:]))

            if word[:i] == reverse[end-i:] and reverse[:end-i] in word_list:
                palingrams.append((reverse[:end-i], word))

print(palingrams)
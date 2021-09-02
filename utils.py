"""
Util module that defines various helper functins
"""

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
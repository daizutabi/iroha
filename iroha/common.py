import os

import iroha


def get_numbers():
    path = os.path.join(os.path.dirname(iroha.__file__),
                        'data/numbers.txt')
    with open(path) as file:
        line = file.read()
    for number in line.split(' '):
        yield int(number)

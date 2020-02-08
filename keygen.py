import string
import random


def generate(count):
    out = str()
    for _ in range(count):
        keys = []
        for _ in range(3):
            keys.append(''.join((random.choice(string.ascii_uppercase + string.digits) for _ in range(5))))
        out += '-'.join(keys) + '\n'
    return out[:-1]


if __name__ == '__main__':
    count = int(input('Укажите нужное кол-во ключей: '))
    keys = generate(count)
    print(keys)

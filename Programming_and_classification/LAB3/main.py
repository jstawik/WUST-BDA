from bitstring import *


def f21(a: BitArray):
    for idx, _ in enumerate(a):
        a.invert(idx)
        print(a)
        a.invert(idx)


def f22

if __name__ == '__main__':
    f21(BitArray('0b0111001'))

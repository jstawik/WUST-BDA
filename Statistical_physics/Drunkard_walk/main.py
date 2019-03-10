from random import uniform
from multiprocessing import Pool
from math import sqrt
from numpy import logspace


def drunkard(steps=30000):
    position = 0
    for i in range(steps):
        if uniform(0, 1) > .5:
            position += 1
        else:
            position -= 1
    return position


def generate_report(steps=30000, drunkards=10000):
    pool = Pool()
    args = [steps]*drunkards #we need an iterable of arguments for drunkard function
    results = pool.map(drunkard, args)
    pool.close()
    pool.join()
    result = 0
    for i in results:
        result += i**2
    result = sqrt(result / drunkards)
    return drunkards, result


if __name__ == "__main__":

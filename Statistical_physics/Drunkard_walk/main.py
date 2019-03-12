from random import uniform
from multiprocessing import Pool
from time import time
from numpy import logspace, std, polyfit, log, arange
import matplotlib.pyplot as plt
import winsound


def drunkard(steps=30000):
    position = 0
    for i in range(steps):
        if uniform(0, 1) > .5:
            position += 1
        else:
            position -= 1
    return position


def generate_std_report(steps=30000, drunkards=10000):
    pool = Pool()
    args = [steps]*drunkards #we need an iterable of arguments for drunkard function
    data = pool.map(drunkard, args)
    pool.close()
    pool.join()
    return std(data)


def generate_hist(lower=1000, upper=5000, drunkards=50000):
    pool = Pool()
    l_result = pool.map(drunkard, [lower]*drunkards)
    u_result = pool.map(drunkard, [upper]*drunkards)
    plt.hist(x=l_result, bins=upper, histtype='step')
    plt.hist(x=u_result, bins=upper, histtype='step')
    plt.show()


if __name__ == '__main__':
    TS = time()
    space = logspace(1, 5, 50)
    results = []
    for i in space:
        results.append(generate_std_report(steps=int(i)))
    print(results)
    linreg = polyfit(log(space), log(results), 1)
    print(linreg)
    plt.scatter(log(space), log(results))
    plt.plot(log(space), log(space)*linreg[0]+linreg[1])
    plt.title('σ for N steps')
    plt.xlabel('log N')
    plt.ylabel('log σ')
    plt.show()
    generate_hist()
    print("Execution time: "+str(time()-TS))
    # winsound.Beep(500, 300)

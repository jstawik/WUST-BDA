from multiprocessing import Pool
import os
import numpy as np
import time


def drive(i):
    os.system(f'Ising2.exe {i}')


if __name__ == '__main__':
    start_time = time.time()
    temps = [i/100 for i in range(130, 450, 5)]
    pool = Pool(14)
    pool.map(drive, temps)
    pool.close()
    pool.join()
    print("--- %s seconds ---" % (time.time() - start_time))
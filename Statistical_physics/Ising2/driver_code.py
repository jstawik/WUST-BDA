from multiprocessing import Pool
import os
import numpy as np
import time


def drive(i):
    os.system('./Ising-100 '+str(i))


if __name__ == '__main__':
    start_time = time.time()
    temps = [i/100 for i in range(130, 200, 5)]+[i/100 for i in range(201, 300, 1)]+[i/100 for i in range(305, 450, 5)]
    pool = Pool(60)
    pool.map(drive, temps)
    pool.close()
    pool.join()
    print("--- %s seconds ---" % (time.time() - start_time))
from multiprocessing import Pool
import os
import numpy as np
import time


def drive(i):
	 os.system(f'crystals.exe {i}')

if __name__ == '__main__':
	start_time = time.time()
	temps = [i/80 for i in range(1, 128)]
	pool = Pool()
	pool.map(drive, temps)
	pool.close()
	pool.join()
	print("--- %s seconds ---" % (time.time() - start_time))
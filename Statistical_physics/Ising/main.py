import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, l: int, T: int):
        self.lattice = np.full((l, l), fill_value=1, dtype=int)
        self.bound = l
        self.temp = T

    def trial(self, idr, idc):
        energy_diff = sum([self.lattice[idr-1][idc], self.lattice[(idr+1) % self.bound][idc],
                           self.lattice[idr][idc-1], self.lattice[idr][(idc+1) % self.bound]])  \
                      * 2 * self.lattice[idr, idc]
        if np.exp(-energy_diff/self.temp) > np.random.rand():
            return True
        else:
            return False

    def mcs(self):
        for idr, row in enumerate(self.lattice):
            for idc, field in enumerate(row):
                if self.trial(idr, idc):
                    self.lattice[idr, idc] *= -1


if __name__ == '__main__':
    sym = Simulation(100, 100)
    for i in range(2000):
        sym.mcs()
        if i % 50 == 0:
           plt.imshow(sym.lattice, aspect='auto', interpolation='none', origin='lower')
           plt.savefig(f'{i}.png')

    plt.imshow(sym.lattice, aspect='auto', interpolation='none', origin='lower')
    # plt.savefig('py.png')
    plt.show()


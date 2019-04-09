import networkx as nx
from random import choice, shuffle
from time import time
from statistics import mean
import matplotlib.pyplot as plt


def t2_sum(a, b):
    return a[0]+b[0], a[1]+b[1]


class Chamber:
    chamber = nx.DiGraph()
    steps = 0

    def __init__(self, width, height, atoms):
        self.width = width
        self.height = height
        for x in range(width):
            for y in range(height):
                self.chamber.add_node((x, y))
                self.chamber.nodes[(x, y)]['id'] = None
        for x in range(width):
            for y in range(height):
                self.chamber.add_edge((x, y), ((x+1) % self.width, y), weight=(1, 0))
                self.chamber.add_edge(((x+1) % self.width, y), (x, y),  weight=(-1, 0))
                self.chamber.add_edge((x, y), (x, (y+1) % self.height), weight=(0, 1))
                self.chamber.add_edge((x, (y+1) % self.height), (x, y), weight=(0, -1))

        if atoms > width * height:
            print('Chamber empty - number of atoms exceeds number of cells')
        else:
            self.density: float = atoms/(width*height)
            self.atom_history = dict((key, (0, 0)) for key in range(atoms))
            self.atom_location = {}
            tmp = list(self.chamber.nodes)
            shuffle(tmp)
            for i, node in enumerate(tmp[0:atoms]):
                self.chamber.nodes[node]['id'] = i
                self.atom_location[i] = node

    def chamber_step(self):
        for index, atom in self.atom_location.items():
            avail = []
            for neigh in self.chamber[atom]:
                if self.chamber.node[neigh]['id'] is None:
                    avail += (neigh,)
            try:
                new_location = choice(avail)
                change = (self.chamber.edges[atom, new_location]['weight'])
                self.atom_history[index] = t2_sum(change, self.atom_history[index])
                self.atom_location[index] = new_location
            except IndexError:
                pass
        self.steps += 1

    def get_diffusion(self):
        return sum([x**2 + y**2 for x, y in self.atom_history.values()])/(len(self.atom_history)*4*self.steps)


def testing():
    b = Chamber(20, 20, 200)
    TS = time()
    for i in range(1000):
        b.chamber_step()
    print(b.get_diffusion())
    print("Execution time: ", str(time() - TS))


if __name__ == '__main__':
    pass
    # Steps / diffusion:
    res = []
    a = Chamber(20, 20, 200)
    for i in range(0, 500):
        a.chamber_step()
        res.append((a.steps, a.get_diffusion()))
    print(res)
    # density/diffusion
    res = []
    for i in range(10, 400, 10):
        a = Chamber(20, 20, i)
        for _ in range(100):
            a.chamber_step()
        res.append((i, a.get_diffusion()))
    print(res)

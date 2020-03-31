from random import random, uniform
# from tqdm import tqdm
import numpy as np

# visualisation
import seaborn as sns
import matplotlib.pyplot as plt

# SPEED
# from multiprocessing import Pool

# Nodes are required to have the following values:
# name
# decision - takes a value from [-1, 0, 1] (decline, undecided, buy))
# qexpectation - float between 0 and 1
# Percolation threshold = pc = 0.595

import igraph as ig
from random import uniform


class Model:
    # for lattice:
    def __init__(self, side_size: int):
        self.side_size = side_size
        self.graph = self._init_lattice()
        sx = side_size - 1
        sy = int(side_size / 2)
        self.graph.vs.find(f'{sx},{int(sy)}')['decision'] = 1

    # PRIVATE:
    def _init_lattice(self):
        lattice = ig.Graph()
        for i in range(self.side_size):
            for j in range(self.side_size):
                lattice.add_vertex(name=f"{i},{j}",
                                   qexpectation=random(),
                                   decision=0)
        for i in range(self.side_size - 1):
            for j in range(self.side_size - 1):
                lattice.add_edge(f"{i},{j}", f"{i + 1},{j}")
                lattice.add_edge(f"{i},{j}", f"{i},{j + 1}")
        for i in range(self.side_size - 1):
            lattice.add_edge(f"{i},{self.side_size - 1}", f"{i + 1},{self.side_size - 1}")
            lattice.add_edge(f"{self.side_size - 1},{i}", f"{self.side_size - 1},{i + 1}")
        return lattice

    def _decision(self, node, qexp, Q):
        #return qexp - (node * 0.05) < Q
        return qexp < Q

    # PUBLIC:
    def get_GC_size(self):
        return len(self.graph.vs.select(decision=1))

    def one_step(self, q):
        nodes = self.graph.vs.select(decision=1)  # Get nodes that bought product
        for node in nodes:  # iterate over each node
            neighbors = list(
                (filter(lambda x: x['decision'] == 0, node.neighbors())))  # Get its neighbors that not decided
            for neighbor in neighbors:  # iterate over each neighbor
                if self._decision(len([x for x in neighbor.neighbors() if x['decision'] == 1]), random(), q):
                    neighbor['decision'] = 1  # customer buys product
                else:
                    neighbor['decision'] = -1  # customer doesn't buy product

    def steps(self, prev_n: [ig.Vertex], q: float):
        if not prev_n:
            pass
        else:
            next_n = set()
            for n in prev_n:
                neighbours = n.neighbors()
                if self._decision(len([x for x in neighbours if x['decision'] == 1]), random(), q):
                    n['decision'] = 1
                    next_n.update(set(neighbours))
                else:
                    n['decision'] = -1
            next_n = list((filter(lambda x: x['decision'] == 0, next_n)))
            self.steps(next_n, q)

    def lattice_to_array(self):
        array = []
        for i in range(self.side_size):
            row = []
            for j in range(self.side_size):
                row.append(self.graph.vs.find(f'{i},{j}')['decision'])
            array.append(row)
        return array

    # def print_lattice(self):
    #     for i in range(self.side_size):
    #         for j in range(self.side_size):
    #             print(self.graph.vs.find(f'{i},{j}')['decision'], end=' ')
    #         print('')



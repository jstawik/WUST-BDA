import igraph as ig
from random import uniform
import seaborn as sns

# Nodes are required to have the following values:
# name
# decision - takes a value from [-1, 0, 1] (decline, undecided, buy))
# qexpectation - float between 0 and 1


class Model:
    # for lattice:
    def __init__(self, n: int):
        self.n = n
        self.g = self.get_lattice()

    def decision(self, Q):
        if self.n <= -2:
            return False
        elif self.n < 2:
            return (self.n + 2)* 0.22 > uniform(0, 1)
        else:
            return 0.88 > uniform(0, 1)

    def get_lattice(self):
        lattice = ig.Graph()
        for i in range(self.n):
            for j in range(self.n):
                lattice.add_vertex(name=f"{i},{j}"
                                   , decision=0
                                   , qexpectation=uniform(0, 1))
        for i in range(self.n-1):
            for j in range(self.n-1):
                lattice.add_edge(f"{i},{j}", f"{i+1},{j}")
                lattice.add_edge(f"{i},{j}", f"{i},{j+1}")
        for i in range(self.n-1):
            lattice.add_edge(f"{i},{self.n - 1}", f"{i + 1},{self.n - 1}")
            lattice.add_edge(f"{self.n - 1},{i}", f"{self.n - 1},{i + 1}")
        return lattice

    def lattice_to_array (self):
        array = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append(self.g.vs.find(f'{i},{j}')['decision'])
            array.append(row)
        return array

    def print_lattice(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.g.vs.find(f'{i},{j}')['decision'], end=' ')
            print('')

    def steps(self, prev_n: [ig.Vertex], q: float):
        if not prev_n:
            pass
        else:
            next_n = set()
            for n in prev_n:
                neighbours = n.neighbors()
                if self.decision(sum(map(lambda x: x['decision'], neighbours, q))):
                    n['decision'] = 1
                else:
                    n['decision'] = -1
                next_n.update(set(filter(lambda x: x['decision'] == 0, neighbours)))
            next_n = list((filter(lambda x: x['decision'] == 0, next_n)))
            self.steps(next_n, q)


if __name__ == '__main__':
    n = 100
    network = Model(n)
    sx = int(n/2)
    sy = 0  # int(n/2)
    # print_lattice(network, n)
    network.g.vs.find(f'{sx},{int(sy)}')['decision'] = 1
    network.steps(network.g.vs.find(f'{sx},{sy}').neighbors(), .7)
    x = sns.heatmap(network.lattice_to_array())

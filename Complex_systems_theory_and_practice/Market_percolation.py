import igraph as ig
from random import uniform

# Nodes are required to have the following values:
# name
# decision (which takes a value from -1, 0, 1 (decline, undecided, buy))


def decision(n: int):
    if n <= -1:
        return False
    elif n < 3:
        return (n + 1) * 0.3 > uniform(0, 1)
    else:
        return 0.9 > uniform(0, 1)


def get_lattice(n: int):
    lattice = ig.Graph()
    for i in range(n):
        for j in range(n):
            lattice.add_vertex(name=f"{i},{j}", decision=0)
    for i in range(n-1):
        for j in range(n-1):
            lattice.add_edge(f"{i},{j}", f"{i+1},{j}")
            lattice.add_edge(f"{i},{j}", f"{i},{j+1}")
    for i in range(n-1):
        lattice.add_edge(f"{i},{n - 1}", f"{i + 1},{n - 1}")
        lattice.add_edge(f"{n - 1},{i}", f"{n - 1},{i + 1}")
    return lattice


def print_lattice(g: ig.Graph, n: int):
    for i in range(n):
        for j in range(n):
            print(g.vs.find(f'{i},{j}')['decision'], end=' ')
        print('')


def steps(prev_n: [ig.Vertex]):
    if not prev_n:
        pass
    else:
        next_n = set()
        for n in prev_n:
            neighbours = n.neighbors()
            if decision(sum(map(lambda x: x['decision'], neighbours))):
                n['decision'] = 1
            else:
                n['decision'] = -1
            next_n.update(set(filter(lambda x: x['decision'] == 0, neighbours)))
        next_n = list((filter(lambda x: x['decision'] == 0, next_n)))
        steps(next_n)


n = 10
network = get_lattice(n)
print_lattice(network, n)
network.vs.find(f'{3},{3}')['decision'] = 1
steps(network.vs.find(f'{3},{3}').neighbors())
print_lattice(network, n)

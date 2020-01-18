import igraph as ig
from random import random

# Nodes are required to have the following values:
# name
# decision (which takes a value from -1, 0, 1 (decline, undecided, buy))


def get_lattice(n: int):
    lattice = ig.Graph()
    for i in range(n):
        for j in range(n):
            lattice.add_vertex(f"{i},{j}")
    for i in range(n-1):
        for j in range(n-1):
            lattice.add_edge(f"{i},{j}", f"{i+1},{j}")
            lattice.add_edge(f"{i},{j}", f"{i},{j+1}")
    for i in range(n-1):
        lattice.add_edge(f"{i},{n - 1}", f"{i + 1},{n - 1}")
        lattice.add_edge(f"{n - 1},{i}", f"{n - 1},{i + 1}")
    return lattice


def steps(prev_n: [ig.Vertex]):
    if not prev_n:
        pass
    else:
        next_n = set()
        for n in prev_n:
            neighbours = n.neighbors()
            # TODO: here we use the above to actually flip the state.
            if (sum(map(lambda x: x['decision'], neighbours))+4 * 0.12) > random.uniform(0, 1):
                # kinda scales the chance from 0 to 86%
                n['decision'] = -1
            else:
                n['decision'] = 1
            next_n.update(set(filter(lambda x: x['decision'] == 0, neighbours)))
        steps(next_n)

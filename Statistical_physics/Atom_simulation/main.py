import networkx as nx
from random import choice, shuffle


class Chamber:
    chamber = nx.Graph()

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
                self.chamber.add_edge((x, y), (x, (y+1) % self.height), weight=(0, -1))
                self.chamber.add_edge((x, (y+1) % self.height), (x, y), weight=(0, -1))

        if atoms > width * height:
            print('Chamber empty - number of atoms exceeds number of cells')
        else:
            self.atom_history = dict((key, []) for key in range(atoms))
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
                self.atom_history[index] += change
                self.atom_location[index] = new_location
            except IndexError:
                pass


if __name__ == '__main__':
    b = Chamber(5, 5, 10)
    a = b.chamber
    print(a)
    print(a.nodes.data())
    print(list(nx.neighbors(a, (3, 3))))
    print(b.atom_history)
    print(b.atom_location)
    for i in range(10):
        b.chamber_step()
        print(b.atom_history)
        print(b.atom_location)

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
                self.chamber.add_edge((x, y), ((x+1) % self.width, y))
                self.chamber.add_edge((x, y), (x, (y+1) % self.height))
        if atoms > width * height:
            print('Chamber empty - number of atoms exceeds number of cells')
        else:
            self.atom_history = dict((key, '') for key in range(atoms))
            self.atom_location = {}
            tmp = list(self.chamber.nodes)
            shuffle(tmp)
            for i, node in enumerate(tmp[0:atoms]):
                self.chamber.nodes[node]['id'] = i
                self.atom_location[i] = node

    def chamber_step(self):
        for atom in self.atom_location:
            neigh = dict(self.chamber[self.atom_location[atom]]).items() #doesnt work
            neigh = list(filter(lambda x: x[1] == {}, neigh))
            print(neigh)# = filter(lambda x: x.key is None, neigh)
            print(list(neigh))


if __name__ == '__main__':
    b = Chamber(5, 5, 20)
    a = b.chamber
    print(a)
    print(a.nodes.data())
    print(list(nx.neighbors(a, (3, 3))))
    print(b.atom_history)
    print(b.atom_location)
    b.chamber_step()

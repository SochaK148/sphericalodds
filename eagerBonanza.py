import matgen as gen


class Graph:
    def __init__(self, v, edges):
        self.vertices = v
        self.edges = [[0 for a in range(v)] for b in range(v)]
        self.colours = [0] * v
        for e in edges:
            self.add_edge(e)

    def add_edge(self, new):
        rx = int(new[0])
        ry = int(new[1])
        self.edges[rx][ry] = 1
        self.edges[ry][rx] = 1

    def is_safe(self, v, colour):
        for i in range(self.vertices):
            if self.edges[v][i] == 1 and self.colours[i] == colour:
                return False
        return True

    def graph_colouring(self, v=0):
        if v == self.vertices:
            return True
        c = 1
        while True:
            if self.is_safe(v, c):
                self.colours[v] = c
                if self.graph_colouring(v+1):
                    return True
            c += 1


v = 4
e = 5
g = Graph(v)
g.edges = gen.rand(v, e)
g.graph_colouring()
for col in g.colours:
    print(col)

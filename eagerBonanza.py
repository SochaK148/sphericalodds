class Graph:
    def __init__(self, v):
        self.vertices = v
        self.edges = [[0 for a in range(v)] for b in range(v)]
        self.colours = [0] * v

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


g = Graph(4)
g.edges = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
g.graph_colouring()
for col in g.colours:
    print(col)

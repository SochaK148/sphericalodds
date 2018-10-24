class Graph:
    def __init__(self, v, edges):
        self.vertices = v
        self.edges = [[0 for _ in range(v)] for _ in range(v)]
        self.colours = [0] * v
        print(edges)
        for e in edges:
            self.add_edge(e)
        # initializing the graph with given edges and vertices

    def add_edge(self, new):
        rx = int(new[0])
        ry = int(new[1])
        self.edges[rx][ry] = 1
        self.edges[ry][rx] = 1
        # adding a given edge to the adjacency matrix

    def is_safe(self, v, colour):
        for i in range(self.vertices):
            if self.edges[v][i] == 1 and self.colours[i] == colour:
                return False
        return True
        # checking if vertex can be coloured with a given colour

    def graph_colouring(self, order, v=0):
        if v == self.vertices:
            return True
        c = 1
        while True:
            if self.is_safe(order[v], c):
                self.colours[order[v]] = c
                if self.graph_colouring(order, v+1):
                    return True
            c += 1
        # greedy algorithm which colours according to given order

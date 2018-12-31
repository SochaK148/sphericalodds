class Graph:
    def __init__(self, v, edges):
        self.vertices = v
        self.edges = [[0 for _ in range(v)] for _ in range(v)]
        self.colours = [0] * v
        self.dfs_verts = []
        self.visited = [0 for _ in range(v)]
        for e in edges:
            self.add_edge(e)
        self.dfs(0)
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

    def check_degree(self, vert):
        degree = 0
        for i in range(len(self.edges)):
            degree += self.edges[i][vert]
        return degree

    def sorted_by_degree(self):
        dict = {}
        for vertice in range(self.vertices):
            dict[vertice] = self.check_degree(vertice)
        return sorted(dict, key=dict.get, reverse=True)

    def dfs(self, i):
        self.dfs_verts.append(i)
        self.visited[i] = 1
        for j in range(self.vertices):
            if self.visited[j] == 0 and self.edges[i][j] == 1:
                self.dfs(j)

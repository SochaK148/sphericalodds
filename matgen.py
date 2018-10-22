import random as rng


def rand(v, e):
    edges = []
    for i in range(e):
        rx = -1
        ry = -1
        while rx == ry or (rx, ry) in edges or (ry, rx) in edges:
            rx = rng.randint(0, v-1)
            ry = rng.randint(0, v-1)
        edges.append((rx, ry))
    return edges


def read(filename):
    edges = []
    with open(filename) as f:
        temp = [line[:-1] for line in f]
        vertices = int(temp[0])
        for line in temp[1:]:
            edges.append([int(x) for x in line.split(' ')])
        return [vertices, edges]

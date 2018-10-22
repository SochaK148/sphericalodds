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
            edges.append([int(x)-1 for x in line.split(' ')])
        return [vertices, edges]


def write(filename, vertices, edge_count):
    f = open('a.txt', 'w')
    f.write(str(vertices) + '\n')
    edges = sorted([sorted([x+1, y+1]) for (x,y) in rand(vertices, edge_count)])
    for [x, y] in edges:
        f.write(str(x) + ' ' + str(y) + '\n')


write('a.txt', 10, 10)

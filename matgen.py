import random as rng

def genAdjMatrix(v, e):
  matrix = [0] * v
  for i in range(v):
    matrix[i] = [0] * v
  for i in range(e):
    edges = []
    rx = -1
    ry = -1
    while rx == ry or (rx,ry) in edges:
      rx = rng.randint(0, v-1)
      ry = rng.randint(0, v-1)
    edges.append((rx,ry))
    matrix[rx][ry] = 1
    matrix[ry][rx] = 1
  return matrix

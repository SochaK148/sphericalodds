import random
from eagerBonanza import Graph


class Monster:
    def __init__(self, vertices):
        self.perm = list(range(vertices))
        random.shuffle(self.perm)
        self.fitness = -1

    def __str__(self):
        return 'Permutation: ' + str(self.perm) + 'Fitness: ' + str(self.fitness)


in_graph = Graph(None, None)
in_vert = None
horde = 20
generations = 1000


def genetics():
    monsters = init_monsters(horde, in_vert)
    for generation in range(generations):
        print('Generation:', str(generation))
        monsters = fitness(monsters)
        monsters = selection(monsters)
        monsters = crossover(monsters)
        monsters = mutation(monsters)
    print('Dawn of the Horde')


def init_monsters(horde, in_vert):
    return [Monster(in_vert) for _ in range(horde)]


def fitness(monsters):
    for monster in monsters:
        in_graph.graph_colouring(monster.perm, in_vert)
        monster.fitness = max(in_graph.colours)
    return monsters


def selection(monsters):
    monsters = sorted(monsters, key=lambda monster: monster.fitness, reverse=True)
    print('\n'.join(map(str, monsters)))
    monsters = monsters[:int(0.2 * len(monsters))]
    return monsters


def crossover(monsters):
    #to-do
    return None


def mutation(monsters):
    #to-do
    return None
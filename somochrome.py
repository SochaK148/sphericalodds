import random
from eagerBonanza import Graph
import matgen as gen


class Monster:
    def __init__(self, vertices):
        self.perm = list(range(vertices))
        random.shuffle(self.perm)
        # a random permutation of vertices the greedy algorithm will use as its order of colouring
        self.fitness = -1

    def __str__(self):
        return 'Fitness: ' + str(self.fitness)


in_graph = None
in_vert = None
horde = 20
generations = 100


def genetics():
    monsters = init_monsters(horde, in_vert)
    for generation in range(generations):
        print('Generation:', str(generation))
        monsters = fitness(monsters)
        monsters = selection(monsters)
        monsters = crossover(monsters)
        # monsters = mutation(monsters)
        # mutation is obsolete
    print('Dawn of the Horde. Result:', monsters[0].fitness)
# wrapper


def init_monsters(horde, in_vert):
    return [Monster(in_vert) for _ in range(horde)]
# initializing our horde of monsters


def fitness(monsters):
    for monster in monsters:
        in_graph.colours = [0] * in_vert
        in_graph.graph_colouring(monster.perm)
        monster.fitness = max(in_graph.colours)
    return monsters
# fitness is simply the number we can color a graph in given order (less=better)


def selection(monsters):
    monsters = sorted(monsters, key=lambda monster: monster.fitness)
    print('\n'.join(map(str, monsters)))
    monsters = monsters[:int(0.2 * len(monsters))]
    return monsters
# selecting monsters with the best fitness


def crossover(monsters):
    children = []
    for _ in range(2*len(monsters)):
        source, filler = random.choice(monsters), random.choice(monsters)
        x = random.randrange(0, len(source.perm) - 1)
        y = random.randrange(x, len(source.perm) - 1)
        child1, child2 = Monster(len(source.perm)), Monster(len(source.perm))
        child1.perm = list(filter(lambda n: n not in source.perm[x:y], filler.perm))
        child1.perm = (child1.perm[:x] + source.perm[x:y] + child1.perm[x:])
        child2.perm = list(filter(lambda n: n not in filler.perm[x:y], source.perm))
        child2.perm = (child2.perm[:x] + filler.perm[x:y] + child2.perm[x:])
        children.extend([child1, child2])
    return monsters + children
# ordered crossover


"""
def mutation(monsters):
    for monster in monsters:
        for _ in range(in_vert//2):
            x, y = 0, 0
            if random.uniform(0.0, 1.0) <= 0.1:
                while x == y:
                    x, y = random.randint(0, in_vert-1), random.randint(0, in_vert-1)
                monster.perm[x], monster.perm[y] = monster.perm[y], monster.perm[x]
    return monsters
"""
# useless code, mutation not necessary for ordered list permutations


if __name__ == '__main__':
    saturation1 = 0.7
    saturation2 = 0.3
    # gen.write("instancja70.txt", in_vert, int(in_vert * (in_vert - 1) * saturation1 * 0.5))
    # gen.write("instancja30.txt", in_vert, int(in_vert * (in_vert - 1) * saturation2 * 0.5))
    [in_vert, edges] = gen.read("instancja70.txt")
    in_graph = Graph(in_vert, edges)
    genetics()

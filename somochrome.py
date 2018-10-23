import random
from eagerBonanza import Graph
import matgen as gen


class Monster:
    def __init__(self, vertices):
        self.perm = list(range(vertices))
        random.shuffle(self.perm)
        self.fitness = -1

    def __str__(self):
        return 'Permutation: ' + str(self.perm) + ' Fitness: ' + str(self.fitness)


in_graph = None
in_vert = None
horde = 200
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
        in_graph.colours = [0] * in_vert
        in_graph.graph_colouring(monster.perm)
        monster.fitness = max(in_graph.colours)
    return monsters


def selection(monsters):
    monsters = sorted(monsters, key=lambda monster: monster.fitness)
    print('\n'.join(map(str, monsters)))
    monsters = monsters[:int(0.2 * len(monsters))]
    return monsters


def crossover(monsters):
    children = []
    for _ in range((horde-len(monsters))//2):
        parent1 = random.choice(monsters)
        parent2 = random.choice(monsters)
        child1 = Monster(in_vert)
        child2 = Monster(in_vert)
        child1.perm, child2.perm = [-1] * in_vert, [-1] * in_vert
        start, end = sorted([random.randrange(in_vert) for _ in range(2)])
        child1_inherited = []
        child2_inherited = []
        for i in range(start, end + 1):
            child1.perm[i] = parent1.perm[i]
            child2.perm[i] = parent2.perm[i]
            child1_inherited.append(parent1.perm[i])
            child2_inherited.append(parent2.perm[i])
        current_p1_position, current_p2_position = 0, 0
        fixed_pos = list(range(start, end + 1))
        i = 0
        while i < in_vert:
            if i in fixed_pos:
                i += 1
                continue

            test_c1 = child1.perm[i]
            if test_c1 == -1:
                p2_trait = parent2.perm[current_p2_position]
                while p2_trait in child1_inherited:
                    current_p2_position += 1
                    p2_trait = parent2.perm[current_p2_position]
                child1.perm[i] = p2_trait
                child1_inherited.append(p2_trait)

            test_c2 = child2.perm[i]
            if test_c2 == -1:
                p1_trait = parent1.perm[current_p1_position]
                while p1_trait in child2_inherited:
                    current_p1_position += 1
                    p1_trait = parent1.perm[current_p1_position]
                child2.perm[i] = p1_trait
                child2_inherited.append(p1_trait)

            i += 1
        children.append(child1)
        children.append(child2)
    monsters.extend(children)
    return monsters


def mutation(monsters):
    for monster in monsters:
        for _ in range(in_vert//2):
            x, y = 0, 0
            if random.uniform(0.0, 1.0) <= 0.1:
                while x == y:
                    x, y = random.randint(0, in_vert-1), random.randint(0, in_vert-1)
                monster.perm[x], monster.perm[y] = monster.perm[y], monster.perm[x]
    return monsters


if __name__ == '__main__':
    [in_vert, edges] = gen.read('a.txt')
    in_graph = Graph(in_vert, edges)
    genetics()

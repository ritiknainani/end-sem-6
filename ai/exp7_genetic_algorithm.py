import random

# Exp 7: Genetic Algorithm
# F(x) = (a + 2b + 3c + 4d) - 30
# Goal: Minimize |F(x)| → fitness = 0 means optimal

def fitness(chromo):
    a, b, c, d = chromo
    return abs((a + 2*b + 3*c + 4*d) - 30)

def create_population(size):
    return [[random.randint(0, 9) for _ in range(4)] for _ in range(size)]

def selection(pop):
    pop.sort(key=fitness)
    return pop[:2]

def crossover(p1, p2):
    pt = random.randint(1, 3)
    return p1[:pt] + p2[pt:], p2[:pt] + p1[pt:]

def mutate(chromo):
    i = random.randint(0, 3)
    chromo[i] = random.randint(0, 9)
    return chromo

def genetic_algorithm():
    pop = create_population(6)

    print("Initial Population (6 chromosomes):")
    for i, c in enumerate(pop):
        val = c[0] + 2*c[1] + 3*c[2] + 4*c[3]
        print(f"  C{i+1}: {c}  F(x)={val}  fitness={fitness(c)}")

    for gen in range(10):
        parents = selection(pop)
        new_pop = [p[:] for p in parents]

        while len(new_pop) < 6:
            c1, c2 = crossover(parents[0][:], parents[1][:])
            new_pop.append(mutate(c1))
            if len(new_pop) < 6:
                new_pop.append(mutate(c2))
        pop = new_pop

    print("\nFinal Population (6 chromosomes):")
    for i, c in enumerate(pop):
        val = c[0] + 2*c[1] + 3*c[2] + 4*c[3]
        print(f"  C{i+1}: {c}  F(x)={val}  fitness={fitness(c)}")

    best = min(pop, key=fitness)
    val = best[0] + 2*best[1] + 3*best[2] + 4*best[3]
    print(f"\nBest Chromosome: {best}")
    print(f"a+2b+3c+4d = {val}")
    print(f"Fitness (distance from 30): {fitness(best)}")

genetic_algorithm()

import random

# Exp 9: Crossover Operation in Genetic Algorithm
# 6 chromosomes, binary, crossover rate = 25%, ONE iteration

POP_SIZE = 6
CHROM_LEN = 5
CROSSOVER_RATE = 0.25

def generate_population():
    pop = []
    for _ in range(POP_SIZE):
        num = random.randint(0, 31)
        pop.append(format(num, f'0{CHROM_LEN}b'))
    return pop

def crossover(population):
    print("\n--- Crossover (Rate = 25%) ---")
    new_pop = population.copy()

    for i in range(0, POP_SIZE, 2):
        if i + 1 >= POP_SIZE:
            break
        p1, p2 = population[i], population[i+1]
        r = random.random()
        print(f"\nPair: {p1} x {p2} | Random = {r:.2f}")

        if r < CROSSOVER_RATE:
            pt = random.randint(1, CHROM_LEN - 1)
            c1 = p1[:pt] + p2[pt:]
            c2 = p2[:pt] + p1[pt:]
            print(f"  Crossover at point {pt}")
            print(f"  Children: {c1}, {c2}")
            new_pop[i], new_pop[i+1] = c1, c2
        else:
            print(f"  No crossover (r >= 0.25)")

    return new_pop

# Main
pop = generate_population()

print("Initial Population (6 chromosomes):")
for i, c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal = {int(c, 2)})")

pop = crossover(pop)

print("\nFinal Population After Crossover:")
for i, c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal = {int(c, 2)})")

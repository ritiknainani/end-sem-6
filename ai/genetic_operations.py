import random

# ---------------- PARAMETERS ----------------
POP_SIZE = 6
CHROMOSOME_LENGTH = 5   # number of bits
CROSSOVER_RATE = 0.25   # 25%
MUTATION_RATE = 0.10    # 10%

# ---------------- INITIAL POPULATION ----------------
def generate_population():
    population = []
    for _ in range(POP_SIZE):
        num = random.randint(0, 31)  # 5-bit number
        binary = format(num, f'0{CHROMOSOME_LENGTH}b')
        population.append(binary)
    return population


# ---------------- CROSSOVER ----------------
def crossover(population):
    print("\n--- Crossover Operation ---")
    new_population = population.copy()

    for i in range(0, POP_SIZE, 2):
        if i+1 >= POP_SIZE:
            break

        parent1 = population[i]
        parent2 = population[i+1]

        r = random.random()

        print(f"\nParents: {parent1}, {parent2}")
        print(f"Random value: {r:.2f}")

        if r < CROSSOVER_RATE:
            point = random.randint(1, CHROMOSOME_LENGTH - 1)

            print(f"Crossover point: {point}")

            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]

            print(f"Children: {child1}, {child2}")

            new_population[i] = child1
            new_population[i+1] = child2
        else:
            print("No crossover")

    return new_population


# ---------------- MUTATION ----------------
def mutation(population):
    print("\n--- Mutation Operation ---")
    new_population = []

    for chrom in population:
        mutated = list(chrom)

        print(f"\nOriginal: {chrom}")

        for i in range(CHROMOSOME_LENGTH):
            r = random.random()

            if r < MUTATION_RATE:
                mutated[i] = '1' if mutated[i] == '0' else '0'
                print(f"Bit {i} mutated")

        mutated_str = ''.join(mutated)
        print(f"After Mutation: {mutated_str}")

        new_population.append(mutated_str)

    return new_population


# ---------------- MAIN ----------------
def main():
    population = generate_population()

    print("Initial Population:")
    for p in population:
        print(p)

    # Crossover
    population = crossover(population)

    print("\nPopulation After Crossover:")
    for p in population:
        print(p)

    # Mutation
    population = mutation(population)

    print("\nFinal Population After Mutation:")
    for p in population:
        print(p)


if __name__ == "__main__":
    main()
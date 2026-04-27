import random

# Exp 10: Mutation Operation in Genetic Algorithm
# 6 chromosomes, binary, mutation rate = 10%, ONE iteration

POP_SIZE = 6
CHROM_LEN = 5
MUTATION_RATE = 0.10

def generate_population():
    pop = []
    for _ in range(POP_SIZE):
        num = random.randint(0, 31)
        pop.append(format(num, f'0{CHROM_LEN}b'))
    return pop

def mutation(population):
    print("\n--- Mutation (Rate = 10%) ---")
    new_pop = []

    for chrom in population:
        bits = list(chrom)
        print(f"\nOriginal: {chrom}")

        for i in range(CHROM_LEN):
            r = random.random()
            if r < MUTATION_RATE:
                bits[i] = '1' if bits[i] == '0' else '0'
                print(f"  Bit {i} flipped! (r = {r:.2f})")

        result = ''.join(bits)
        print(f"After Mutation: {result}")
        new_pop.append(result)

    return new_pop

# Main
pop = generate_population()

print("Initial Population (6 chromosomes):")
for i, c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal = {int(c, 2)})")

pop = mutation(pop)

print("\nFinal Population After Mutation:")
for i, c in enumerate(pop):
    print(f"  C{i+1}: {c} (decimal = {int(c, 2)})")

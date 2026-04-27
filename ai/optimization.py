import random

# -------- Fitness --------
def fitness(x):
    return x**3 - 6*x**2 + 4*x + 12


# -------- Hill Climbing --------
def hill_climb():
    cur = int(input("Initial: "))
    step = int(input("Step: "))
    iters = int(input("Iterations: "))

    for _ in range(iters):
        neighbors = [cur-step, cur+step]
        best = max(neighbors, key=fitness)

        if fitness(best) <= fitness(cur):
            break
        cur = best

    print("Best:", cur, "Fitness:", fitness(cur))


# -------- Genetic Algorithm --------
def genetic():
    size = int(input("Population size: "))
    gen = int(input("Generations: "))
    mut = float(input("Mutation rate: "))

    pop = [random.randint(-10,10) for _ in range(size)]

    for _ in range(gen):
        pop = sorted(pop, key=fitness, reverse=True)

        new_pop = pop[:2]  # elitism

        while len(new_pop) < size:
            p1, p2 = random.sample(pop[:4], 2)
            child = (p1 + p2)//2

            if random.random() < mut:
                child += random.randint(-2,2)

            new_pop.append(child)

        pop = new_pop

    best = max(pop, key=fitness)
    print("Best:", best, "Fitness:", fitness(best))


# -------- MAIN --------
def main():
    while True:
        print("\n1.Hill Climb 2.Genetic 3.Exit")
        ch = input("Choice: ")

        if ch == '3':
            break

        if ch == '1':
            hill_climb()
        elif ch == '2':
            genetic()
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
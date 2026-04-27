import math

# Exp 8: Hill Climbing Algorithm
# Functions: y = sin(x), y = -x^2, y = -5x^2 + 3x + 6

def hill_climbing(func, func_name, initial, step=0.1, iters=100):
    current = initial
    print(f"\nHill Climbing for {func_name}")
    print(f"Initial: x={current:.4f}, y={func(current):.4f}")

    for i in range(iters):
        neighbors = [current - step, current + step]
        best = max(neighbors, key=func)

        if func(best) > func(current):
            current = best
            print(f"Step {i+1}: x={current:.4f}, y={func(current):.4f}")
        else:
            print(f"Converged at step {i+1}")
            break

    print(f"Best: x={current:.4f}, y={func(current):.4f}")

# Menu
while True:
    print("\n--- Hill Climbing ---")
    print("1. y = sin(x)")
    print("2. y = -x^2")
    print("3. y = -5x^2 + 3x + 6")
    print("4. Exit")
    ch = input("Choice: ")

    if ch == '4':
        break

    x0 = float(input("Initial x: "))
    step = float(input("Step size: "))
    iters = int(input("Iterations: "))

    if ch == '1':
        hill_climbing(math.sin, "y = sin(x)", x0, step, iters)
    elif ch == '2':
        hill_climbing(lambda x: -(x**2), "y = -x^2", x0, step, iters)
    elif ch == '3':
        hill_climbing(lambda x: -5*x**2 + 3*x + 6, "y = -5x^2+3x+6", x0, step, iters)

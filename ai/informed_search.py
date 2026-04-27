import heapq

# -------- Greedy Best First --------
def greedy(graph, h, start, goal):
    visited = set()
    pq = [(h[start], start)]

    print("Greedy:")

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        visited.add(node)

        for nbr, cost in graph.get(node, []):
            if nbr not in visited:
                heapq.heappush(pq, (h[nbr], nbr))

    print("\nGoal Not Found")


# -------- A* --------
def astar(graph, h, start, goal):
    visited = set()
    pq = [(h[start], 0, start)]  # (f, g, node)

    print("A*:")

    while pq:
        f, g, node = heapq.heappop(pq)

        if node in visited:
            continue

        print(f"{node}(g={g},h={h[node]})", end=" ")

        if node == goal:
            print(f"\nGoal Found, Cost={g}")
            return

        visited.add(node)

        for nbr, cost in graph.get(node, []):
            if nbr not in visited:
                new_g = g + cost
                new_f = new_g + h[nbr]
                heapq.heappush(pq, (new_f, new_g, nbr))

    print("\nGoal Not Found")


# -------- MAIN --------
def main():
    graph = {
        'A': [('B',1),('C',3)],
        'B': [('D',3),('E',1)],
        'C': [('F',5)],
        'D': [],
        'E': [('G',2)],
        'F': [],
        'G': []
    }

    h = {'A':6,'B':4,'C':5,'D':3,'E':2,'F':4,'G':0}

    while True:
        print("\n1.Greedy 2.A* 3.Exit")
        ch = input("Choice: ")

        if ch == '3':
            break

        s = input("Start: ")
        g = input("Goal: ")

        if ch == '1':
            greedy(graph, h, s, g)
        elif ch == '2':
            astar(graph, h, s, g)
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
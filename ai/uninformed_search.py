from collections import deque

# ---------------- DFS ----------------
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")

    if start == goal:
        return True

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False


# ---------------- DLS ----------------
def dls(graph, start, goal, limit, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")

    if start == goal:
        return True

    if limit <= 0:
        return False

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, limit - 1, visited):
                return True
    return False


# ---------------- DFID ----------------
def dfid(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth = {depth}: ", end="")
        if dls(graph, start, goal, depth):
            print("\nGoal Found!")
            return
    print("\nGoal Not Found")


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    print("BFS:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    print("\nGoal Not Found")


# ---------------- MAIN ----------------
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }

    while True:
        print("\n1.DFS 2.DLS 3.DFID 4.BFS 5.Exit")
        ch = input("Choice: ")

        if ch == '5':
            break

        s = input("Start: ")
        g = input("Goal: ")

        if ch == '1':
            print("DFS:", end=" ")
            print("\nGoal Found!" if dfs(graph, s, g) else "\nGoal Not Found")

        elif ch == '2':
            limit = int(input("Limit: "))
            print("DLS:", end=" ")
            print("\nGoal Found!" if dls(graph, s, g, limit) else "\nGoal Not Found")

        elif ch == '3':
            depth = int(input("Max Depth: "))
            dfid(graph, s, g, depth)

        elif ch == '4':
            bfs(graph, s, g)

        else:
            print("Invalid")

if __name__ == "__main__":
    main()
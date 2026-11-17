
from collections import deque

# Create Graph
graph = {}

n = int(input("Enter Number of Nodes: "))

for i in range(n):
    node = input(f"\nEnter Node {i+1}: ")
    graph[node] = []

    neighbours = int(input(f"Enter Number of Neighbours of {node}: "))

    for j in range(neighbours):
        neighbour = input(f"Enter Neighbour {j+1}: ")
        graph[node].append(neighbour)

# Display Graph
print("\nGraph:")
for node in graph:
    print(node, ":", graph[node])

# Start and Goal
start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

# Breadth First Search
def bfs(start, goal):
    visited = []
    queue = deque()

    queue.append(start)
    visited.append(start)

    print("\n===== BFS =====")

    while queue:
        current = queue.popleft()

        print("--------------------------------")
        print("Current Node:", current)
        print("Queue:", list(queue))
        print("Visited:", visited)

        if current == goal:
            print("\nGoal Found!")
            print("Visited Path:", visited)
            return

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

                print("Added:", neighbour)
                print("Queue:", list(queue))
                print("Visited:", visited)

    print("\nGoal Not Found!")


# Depth First Search
def dfs(start, goal):
    visited = []
    stack = []

    stack.append(start)

    print("\n===== DFS =====")

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            print("--------------------------------")
            print("Current Node:", current)
            print("Stack:", stack)
            print("Visited:", visited)

            if current == goal:
                print("\nGoal Found!")
                print("Visited Path:", visited)
                return

            for neighbour in reversed(graph[current]):
                if neighbour not in visited:
                    stack.append(neighbour)

                    print("Added:", neighbour)
                    print("Stack:", stack)

    print("\nGoal Not Found!")


# Menu
while True:
    print("\n******* MENU *********")
    print("1. Breadth First Search")
    print("2. Depth First Search")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        bfs(start, goal)

    elif choice == 2:
        dfs(start, goal)

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

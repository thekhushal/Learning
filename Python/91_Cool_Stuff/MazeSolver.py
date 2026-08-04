# Maze: 1 = path, 0 = wall
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1]
]

# Maze size
N = len(maze)

# Empty solution matrix
solution = [[0 for _ in range(N)] for _ in range(N)]

def print_maze(m):
    for row in m:
        for val in row:
            print(val, end=" ")
        print()

def is_safe(maze, x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1

def solve_maze(x, y):
    if x == N - 1 and y == N - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y):
        solution[x][y] = 1

        # Move Down
        if solve_maze(x + 1, y):
            return True

        # Move Right
        if solve_maze(x, y + 1):
            return True

        # Move Up
        if solve_maze(x - 1, y):
            return True

        # Move Left
        if solve_maze(x, y - 1):
            return True

        # Backtrack
        solution[x][y] = 0
        return False

    return False

# Execution
print("Maze:")
print_maze(maze)

if solve_maze(0, 0):
    print("\nPath from Start to Finish:")
    print_maze(solution)
else:
    print("\nNo path found in the maze.")

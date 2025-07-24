# 9x9 Sudoku grid, 0 represents empty cells
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_grid(g):
    for row in g:
        for val in row:
            print(val, end=" ")
        print()

def find_empty(g):
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                return i, j  # row, col
    return None

def is_valid(g, num, row, col):
    for i in range(9):
        if g[row][i] == num:
            return False
        if g[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if g[start_row + i][start_col + j] == num:
                return False

    return True

def solve(g):
    find = find_empty(g)
    if not find:
        return True  # Solved

    row, col = find

    for num in range(1, 10):
        if is_valid(g, num, row, col):
            g[row][col] = num

            if solve(g):
                return True

            g[row][col] = 0  # backtrack

    return False

# Execution
print("Sudoku Puzzle:")
print_grid(grid)

if solve(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")

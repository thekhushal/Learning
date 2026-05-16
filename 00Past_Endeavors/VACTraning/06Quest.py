def issafe(i, j, m, r, c):
    return 0 <= i < r and 0 <= j < c and m[i][j] == 1


def func(i, j, m, s, r, c):
    if i == r - 1 and j == c - 1 and m[i][j] == 1:
        s[i][j] = 1
        return True

    if issafe(i, j, m, r, c):
        s[i][j] = 1

        if func(i + 1, j, m, s, r, c):
            return True

        if func(i, j + 1, m, s, r, c):
            return True

        s[i][j] = 0

    return False


r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

m = []
for _ in range(r):
    m.append(list(map(int, input().split())))

s = [[0 for _ in range(c)] for _ in range(r)]

if func(0, 0, m, s, r, c):
    print("Path found! Solution matrix:")
    for row in s:
        print(row)
else:
    print("No path exists from start to destination.")

def func (r, c):
    if r == 0 or c == 0:
        return 1
    return func(r-1, c) + func(r, c-1)

r = int (input ("Enter: "))
c = int (input ("Enter: "))

print(func(r-1, c-1))
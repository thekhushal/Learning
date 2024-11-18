# Fibonachi = 1,1,2,3,5,8,13,21,34
# # Start with 4th, go for 5 elements => 3, 5, 8, 13, 21
p = int(input("Starting no. : "))
q = p
i = 1 #int(input("How long shall Fibonachi Sequence be continued : "))
print(p)
print(q)
while i - 2 >= 1 :
    q = p + q
    print(q)
    p = q - p
    i -= 1
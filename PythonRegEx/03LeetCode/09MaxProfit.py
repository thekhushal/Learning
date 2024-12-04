sp = [7, 1, 5, 3, 6, 4]

# buy = sp [0]
# sell = sp[1]
# profit = 0

# for x in range(len(sp)):
#     difference = sp[x] - buy
#     profit = max(profit, difference)
#     buy = min(buy, sp[x])

# print(profit)

# _______________________________________________________________________________________
# Solution 2
# Time Complixity = O(n^2)
# MaxProfit = 0

# for x in range(len(SP)):
#     for y in range(x + 1, len(SP)):
#         if SP[y] - SP[x] >= MaxProfit:
#             MaxProfit = SP[y] - SP[x]

# print(MaxProfit)
# ___________________________________________________________________________________

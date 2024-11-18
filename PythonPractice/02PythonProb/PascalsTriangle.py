# 1                                         # O     # 1
# 1   1                                     # E     # 2
# 1   2   1                                 # O     # 3
# 1   3   3   1                             # E     # 4
# 1   4   6   4   1                         # O     # 5
# 1   5   10  10  5   1                     # E     # 6
# 1   6   15  20  15  6   1                 # O     # 7
# 1   7   21  35  35  21  7   1             # E     # 8
# 1   8   28  56  70  56  28  8   1         # O     # 9
# 1   9   36  84  126 126 84  36  9   1     # E     # 10
lenSeries = int(input("Length of Series : "))

lastSeries = []

a = 0
while a <= lenSeries :

    b = 0
    seriesInConti = []
    while b <= a :
        if b == 0 :
            print("1", end = "")
            seriesInConti.append(1)
            --
        if b == a :
            print("1", end = "\n")
            seriesInConti.append(1)
        
        else :
            num = lastSeries[b] + lastSeries[b-1]
            print(num)
            seriesInConti.append(num)
        b += 1
    lastSeries = seriesInConti 
    a += 1

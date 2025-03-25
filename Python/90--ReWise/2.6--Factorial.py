print("#ThisIsFactorilCalculator")
Fact = int(input("Find the factorial of : "))
if Fact == 0 :
    print("Number of ways to arrange a data set with no values in it is 1")

Factorial = Fact
while 1 < Fact :
    Fact -= 1
    Factorial *= Fact
print(Factorial)
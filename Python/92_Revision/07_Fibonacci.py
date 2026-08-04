Fibbi = int(input("Print the Fibbi till : "))

Start, fibonachi = 1, 1

print(Start)

while fibonachi < Fibbi : 
    print(fibonachi)
    PreVal = fibonachi
    fibonachi += Start
    Start = PreVal


"""Fibbi = int(input("Print the Fibbi till : "))

PreVal, NewVal = 1, 1

print(PreVal)

while NewVal < Fibbi :
    print(NewVal)
    fibonachi = PreVal + NewVal
    PreVal = NewVal
    NewVal = fibonachi"""
    
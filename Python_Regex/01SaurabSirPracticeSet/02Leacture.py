# __________________________________________________________________________
# Problem 1
# ProductName = []
# Quantity = []

# while (True):
#     Product = input("What would you like to buy: ")
#     NoOfItem = int(input("How much would you like to buy: "))
    
#     if NoOfItem >= 10:
#         ProductName.append(Product)
#         Quantity.append(NoOfItem)
#     else:
#         print("The minimum number of products to be purchased is 10")

#         ask = input("Would you like to reorder: (y/n) ")
#         if ask == "y":
#             continue
#         else:
#             break

#     ask = input("Would you like to order anything else: (y/n) ")
#     if ask == "y":
#         continue
#     else:
#         break
    
# print(ProductName)

# print(Quantity)
# _____________________________________________________________________________




# _____________________________________________________________________________
# Problem 2
# Students = []
# Scores =[]

# while True:
#     Students.append(input("Enter student name: "))
#     Scores.append( int( input("How much did he score: ")))

#     ask = input("Is there another student: (y/n) ")
#     if ask == "y":
#         continue
#     else:
#         break

# print("\nBellow you'll find the result's of all the students: ")
# for i in range(0,len(Students)):
#     if Scores[i] < 40 :
#         print(Students[i], " : Fail")
#     else:
#         print(Students[i], " : Pass")

# print("\nBellow you'll find some stactistics based on result of students: ")

# sum = 0
# for i in range(0,len(Students)):
#     sum += Scores[i]
# print("- Average result is students is ", sum / len(Scores))

# highest = Scores[0]
# for i in range(1,len(Students)):
#     if highest < Scores[i]:
#         highest = Scores[i]
# print("- Highest marks scored by someone is ",highest)

# lowest = Scores[0]
# for i in range(1,len(Students)):
#     if lowest > Scores[i]:
#         lowest = Scores[i]
# print("- Lowest marks scored by someone is ",lowest)
# ______________________________________________________________________________________




# _______________________________________________________________________________________
# Problem 3
# Denomination100 = 200
# Denomination500 = 40
# Denomination2000 = 30

# Total = (Denomination100 * 100) + (Denomination500 * 500) + (Denomination2000 * 2000)

# print("---WELCOME---")
# while Total > 100:
#     RequestedAmount = int(input("How much would you like to widraw: "))

#     if RequestedAmount % 100 != 0:
#         print("Requested ammount must be in multiples of 100")

#         ask = input("Would you like to continue: (y/n)")
#         if ask == "y":
#             continue
#         else:
#             break
#     elif RequestedAmount > Total:
#         print("Insufficient balance")

#     Output2000 = RequestedAmount // 2000
#     RequestedAmount -= (Output2000*2000)
#     Output500 = RequestedAmount // 500
#     RequestedAmount -= (Output500*500)
#     Output100 = RequestedAmount // 100
#     RequestedAmount -= (Output100*100)

#     Denomination100 -= Output100
#     Denomination500 -= Output500
#     Denomination2000 -= Output2000
#     Total = (Denomination100 * 100) + (Denomination500 * 500) + (Denomination2000 * 2000)

#     print("Paid")
#     print(f"{Output100} 100 rupee note \n{Output500} 500 rupee note \n{Output2000} 2000 rupee note")

#     ask = input("Would you like to continue: (y/n)")
#     if ask == "y":
#         continue
#     else:
#         print("Remaning Balance", Total)
#         break
# __________________________________________________________________________________________




# ___________________________________________________________________________________________
# Problem 4

# print("---WELCOME---")

# salary = int(input("Whats your salary: "))
# CreditScore = int(input("Whats your Credit Score: "))
# YearsEmployed = int(input("For how long have you been employed: "))

# if salary > 50000 & CreditScore > 700 & YearsEmployed > 2:
#     print("Loan approved")
# else:
#     print("Loan not approved")
# ____________________________________________________________________________________________



# ____________________________________________________________________________________________
# Problem 5
# TotalCapacity = 5
# CurrentCapacity = 0

# while True:
#     status = input("Parking (p) || Leaving(L) : ")

#     if status == "p" or status == " " :
#         CurrentCapacity += 1
#         if CurrentCapacity > TotalCapacity :
#             CurrentCapacity -= 1
#             print("No space, parking is full")
#     else:
#         CurrentCapacity -= 1
#         if CurrentCapacity < 0 :
#             CurrentCapacity += 1
#             print("No space, parking is full")

#     ask = input("Would you like to continue: (y/n)")
#     if ask == "y":
#         continue
#     else:
#         print(CurrentCapacity)
#         break
# ______________________________________________________________________________________________



# ______________________________________________________________________________________________
# Problem 6

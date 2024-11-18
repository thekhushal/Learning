# Q.1 Write a Python program that takes a user's age as input and determines if the person is eligible to vote.

# age = int(input("Whats your age: "))
# if age >= 18:
#     print("You are elegible to vote")
# else:
#     print("Better luck next time :)")

# _______________________________________________________________________________________________________________

# _______________________________________________________________________________________________________________
# Q.2 A store offers a discount of 10% if the total purchase amount exceeds $100. Write a program that asks the user for the total purchase amount and calculates the final price after applying the discount if applicable.

# total = int(input("Total cart value: "))

# if total < 100:
#     print("No discount applicable on orders bellow $100")
# else:
#     final = total - (total / 10)
#     print("Final Price: ", final)
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
# Q.3  A cinema charges different ticket prices based on age:
# Children (under 12): $7
# Adults (12 to 60): $10
# Seniors (above 60): $8
# Write a Python program that asks for the user's age and prints the ticket price accordingly.


# age = int(input("What's your age: "))

# if age < 12:
#     print("Ticket Price $7")
# elif 12 <= age < 60 :
#     print("Ticket Price $10")
# else :
#     print("Ticket Price $8")
# _______________________________________________________________________________________________________________


# _______________________________________________________________________________________________________________
# Q.4  Write a Python program that checks if a person is eligible for a loan based on their income and credit score. The person is eligible if their income is above $50,000 and their credit score is above 650.

# income = int(input("How much do you earn: "))
# creditscore = int(input("What's your credit score:  "))

# if income >= 50000 and creditscore >= 650:
#     print("Elegible for loan :)")
# else:
#     print("Not elegible :(")
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
# Q.5  A gym offers different types of memberships:
# Gold: $100/month for unlimited access
# Silver: $70/month for access 5 times a week
# Bronze: $50/month for access 3 times a week
# Write a Python program that asks the user how many times per week they plan to visit the gym and suggests the best membership option.

# ask = int(input("How many days per week do you plan to visit our gym: "))

# if ask <= 3:
#     print("A Bronze memmbership that offers 3 visits per week would suit the best ")
# elif 3 < ask <= 5:
#     print("A Silver memmbership that offers 5 visits per week would suit the best ")
# else:
#     print("A Gold memmbership that offers Unlimited visits per week would suit the best ")
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
# Q.6  A company offers free delivery for orders above $50 within the city, but charges $5 for deliveries outside the city. Write a Python program that asks the user for the order amount and location (inside or outside the city) and calculates the total amount including any delivery charges.

# print("NOTE - To calculate final amount including delivery follow instructions")
# CartValue = int(input("Enter your order value: "))
# Location = input("City (c) | Outskirts (o): ")

# if CartValue < 50:
#     print("Delivery charge of $2 per km is ")
#     distance = int(input("How far are you: "))
#     total = CartValue + (distance * 2)
#     print("Total bill: ", total)
# elif CartValue >= 50:
#     if Location == "c" :
#         print("Total bill: ", CartValue)
#     else: 
#         print("Total bill: ", (CartValue + 5))
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
#  Q.7 A parking lot charges $5 for the first 2 hours and $3 for every additional hour. Write a program that takes the number of hours a vehicle was parked as input and calculates the total parking fee.

# hours = int(input("How long were you parked: "))

# if hours <= 2:
#     print("Bill = $5" )
# else:
#     bill = 5 + ((hours - 2)*3)
#     print("Bill = ", bill)
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
# Q.8  An electricity company charges different rates based on usage:

# First 100 units: $0.10/unit
# Next 100 units: $0.15/unit
# Above 200 units: $0.20/unit
# Write a program that asks the user for the number of units consumed and calculates the total bill.

# units = int(input("How many units did you consume: "))

# if units <= 100:
#     print("Bill = ", (units * 0.10))
# elif 100 < units < 200:
#     bill = 10 + ((units-100) * 0.15)
#     print("Bill = ", bill)
# else: 
#     bill = 25 + ((units-200) * 0.20)
#     print("Bill = ", bill)
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
# Q.9  Write a Python program that takes a student's exam score as input and prints their grade based on the following:
# Score >= 90: Grade A
# Score 80–89: Grade B
# Score 70–79: Grade C
# Score 60–69: Grade D
# Score < 60: Grade F

# Score = int(input("How much did you score: "))

# if Score >= 90:
#     print("Grade A")
# elif 80 <= Score < 90:
#     print("Grade B")
# elif 70 <= Score < 80:
#     print("Grade C")
# elif 60 <= Score < 70:
#     print("Grade D")
# else:
#     print("Grade F")
# _______________________________________________________________________________________________________________



# _______________________________________________________________________________________________________________
#Q.10  An airline allows a free baggage allowance of 15kg. If the baggage exceeds 15kg, the passenger is charged $10 per extra kilogram. Write a Python program that asks for the weight of the baggage and calculates the total charge if any.

# BagWeight =  int(input("How much does your lugage weight: "))

# if BagWeight <= 15:
#     print("No extra charges :)")
# else: 
#     charges = (BagWeight - 15) * 10
#     print("Total = ", charges)
# _______________________________________________________________________________________________________________
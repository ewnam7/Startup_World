print ("Trying Dictionary function today")

# name = "Creisttiano Raymond Thomas"
# age = 30
# height = 1.85
# is_student = True

# Skills = ["Trader", "Python programmer","Entrepreneur", "Investor", "Teacher"]

# profile = {
#     "name" : name,
#     "age" : age,
#     "height": height,
#     "Skills": Skills,
#     }
# #print(f"My name is {profile['name']} and I know {profile['Skills'][0]}")
# print ("My name is + {profile['name']} and I know + {profile['Skills'][0]}")

name = input("Enter your name: ")
age  = input("Enter your age: ")
country = input ("Which country are you from? ")

#Loan Details
loan_amount = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate (in %): "))
Number_Of_Years = int(input("Enter the number of years for the repayment:")) 

profile = {
    "name" : name,
    "age" : age,
    "country" : country
}

#Basic Loan Calculation
monthly_payment = (loan_amount * (1 + (interest_rate/100))) / (Number_Of_Years * 12)

print(f"The loan taker name is {profile ['name']}, the person is {profile ['age']} years old and he is from {profile ['country']}")
print(f"The amount of loan is {loan_amount}, the calculated interest rate is {interest_rate}% and the number of years for repayment is {Number_Of_Years} years.")
print(f"The monthly payment for the loan is: {monthly_payment:.2f}")



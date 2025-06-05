print ("Day 3: Learn to make Python to think and make decisions")
print("Creating eligibility checker for loan")

# print ("Task 1: Trying IF & Else")
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eleigible to vote!")

# else:
#     print("You are not eligible to vote yet!")

#------------------------------------------------
# print ("Task 2: Trying if, elif & else")

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Excellent score!")

# elif marks >= 80:
#     print("You did well ")

# elif marks >= 70:
#     print("You did good. You can do better!")

# else:
#     print("You need to work hard. You can do it!")

#------------------------------------------------
age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18 and country.lower() == "malaysia":
    print("You are eligible to to get loan!")

else:
    print("You are not eligible to get loan yet!")
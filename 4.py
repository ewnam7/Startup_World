# print("Day 4: Using while loop to check authority")

# while True:
#     count = 0
#     while count < 4:
#         password = input("Please enter your password:")
#         if len(password) >= 8 and "@" in password:
#             print("Password is strong.")
#             break

#         else:
#             print("Password must be at least 8 characters long and contain '@'. Please try again.") 
#             count += 1

#     if count == 4:
#         print("You have entered the wrong password many times. Access denied.")

print("Day 4: Using while loop to check Door authority")
attempts = 0
code_code = "2580"
max_attempts = 3
while attempts < max_attempts:
    door_password = input("Please enter the door password: ")
    if not door_password.isdigit():
        print("Password must be numeric. Please try again.")
        attempts += 1

    elif door_password == code_code:
        print("Access granted. You may enter.")
        break

    else:
        print("Incorrect password. Please try again.")
        attempts += 1

if attempts == max_attempts:
    print("Security alert: System locked!")
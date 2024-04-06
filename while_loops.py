# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# while loop

number = 1
print(number)

while number <= 5: 
    print(number)
    number += 1

login_attempts = 5
user_password = "password"

while login_attempts > 0:
    password = input("Enter password: ")
    if (password != user_password):
        print("Wrong password")
        login_attempts -= 1
        print(f"Remaining attemps: {login_attempts}")

        if (login_attempts == 0):
            print("You ran out of attemps, please contact your administrator.")
    else:
        print("Login successful")
        break
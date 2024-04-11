# Check if a number is prime or not

def check_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            print("Not a prime number")
            break
    else:
        print("It is a prime number")

check_prime(13)
check_prime(9)
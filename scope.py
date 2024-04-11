# Scope - global and local
# Global - Accessible anywhere
# Local - Accessible only inside function where declared

fname = "Peter" # Global variables
lname = "Parker" # Global variables

def greet():
    fname = "Tony" # Local variables
    lname = "Stark" # Local variables

    print("Inside Function")
    print(f"Jarvis: \"Hello, {fname} {lname}!\"")
    print(" ")

print("Outside of Function")
print(f"Aunt May: \"Hello, {fname} {lname}!\"")
print(" ")

greet()
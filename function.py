# Functions - collection of code that performs a single task
# Starts with 'def' keyword
# Then has the name of the function
# Optional list of arguments (inputs to the function)
# Optional - return statement (output of the function)

first_name = 'Hayden'
last_name = "Bradford"

def greet(fname, lname):
    print(f"Hello World! {fname} {lname}")

greet("Hayden", "Bradford") # Need to call the function for it to run - strings for arguments

greet(first_name, last_name) # Variables for arguments
# John Doe -> dairyfarm

first_name = input("First Name: ")
last_name = input("Last Name: ")
company = input("Company Name: ").replace(" ", "")

email = f"{first_name}.{last_name}@{company}.com.au".lower()

print(email)
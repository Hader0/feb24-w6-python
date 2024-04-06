# List all numbers from 1 - 100, state whether they are odd or even

list_even = []
list_odd = []

for i in range(1, 101):
    if (i % 2 == 0):
        list_even.append(i)
    else:
        list_odd.append(i)

print(f"Even List: {list_even}")
print("\n")
print(f"List Odd: {list_odd}")
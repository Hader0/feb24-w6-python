# Non-primitave data types - hold/store multiple pieces of data
# List/Array - Collection of data - indexed - mutable (changed)

numbers = [1, 2, 3, 4, 5] 

print(numbers[0])

numbers.append(6)
print(numbers)

numbers.insert(6, 7)
print(numbers)

numbers.remove(1)
print(numbers)

print(len(numbers))

print(numbers.sort())
print(numbers.reverse())


# Tuple - Collection of data - indexed - immutable (Cannot be changed)

names = ["John", "Jane", "Mike"]
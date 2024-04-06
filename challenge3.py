# palindrome - string reversed is also the same as the original string (E.g. racecar)

word = "racecar"

word_reversed = ""

# Lengthy way of reversing a string
for letter in word:
    word_reversed = letter + word_reversed

if (word_reversed == word):
    print(f"\"{word_reversed}\" is a palindrome")
else:
    print(f"\"{word_reversed}\" is not a palindrome")


# Easy way of reversing a string
if (word[::-1] == word):
    print(f"\"{word_reversed}\" is a palindrome")
else:
    print(f"\"{word_reversed}\" is not a palindrome")
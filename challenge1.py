# count vowels and consonants in a string
# count the number of capital letters
# remove spaces from string without string methods


sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

num_vowel = 0
num_consonant = 0
num_upper_case = 0

for letter in sentence:

    if letter.isupper():
        num_upper_case += 1

    if letter in '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ':
        continue # Meaning go to the next loop and skips the remaining lines below

    if letter.lower() in 'aeiou':
        num_vowel += 1
    else:
        num_consonant += 1

print(f"Number of vowels: {num_vowel}")
print(f"Number of consonants: {num_consonant}")
print(f"Number of upper case characters: {num_upper_case}")

# Getting the paragraph without spaces

sentence_without_space = ""

for letter in sentence:
    if letter != " ":
        sentence_without_space += letter

print(sentence_without_space)
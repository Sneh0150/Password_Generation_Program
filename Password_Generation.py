import random

# Define character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '.']

print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

# Generate the password components
password_chars = []

for i in range(num_letters):
    random_char= random.choice(letters)
    password_chars.append(random_char)

for i in range(num_symbols):
    random_char=random.choice(symbols)
    password_chars.append(random_char)

for i in range(num_numbers):
    random_char=random.choice(numbers)
    password_chars.append(random_char)

# Shuffle the password characters to ensure randomness
random.shuffle(password_chars)

print(password_chars)

# Convert list to string
password = ''.join( map(str,password_chars))

print(f"Your password generated is: {password}")
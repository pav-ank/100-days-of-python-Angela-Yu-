from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
import random

password = ""
for L in range(1, nr_letters + 1):
    rand_letters = random.choice(letters)
    password += rand_letters
for S in range(1, nr_symbols + 1):
    rand_symbols = random.choice(symbols)
    password += rand_symbols
for N in range(1, nr_numbers + 1):
    rand_numbers = random.choice(numbers)
    password += rand_numbers

# password_list = password
# print(password_list)

#hard level
password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)# When you use "".join(password_list), it combines all the individual characters in the password_list into a single string.
print(shuffled_password)


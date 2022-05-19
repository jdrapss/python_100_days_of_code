#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# random_numbers = ''
# random_symbols = ''
# random_letters = ''

# for letter in range(0, nr_letters):
#   random_letters += random.choice(letters)

# for symbol in range(0, nr_symbols):
#   random_symbols += random.choice(symbols)

# for number in range(0, nr_numbers):
#   random_numbers += random.choice(numbers)

# password = random_letters + random_symbols + random_numbers
# print(password) # Prints random letters random symbols and random numbers all in one row
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# random_numbers = ''
# random_letters = ''
# random_symbols = ''

# for number in range(0, nr_numbers):
#   random_numbers += random.choice(numbers)

# for letter in range(0, nr_letters):
#   random_letters += random.choice(letters)

# for symbol in range(0, nr_symbols):
#   random_symbols += random.choice(symbols)

# password_list = [random_numbers, random_letters, random_symbols]

# random_list = random.sample(password_list, len(password_list))
# random_password = ''.join(random_list) # Can also make an empty password list and make a for look for each character in random_list
# print(random_password)

# Can also create a password list that is empty at the top and make each for loop add the random choice to that password_list

password_list = []
for number in range(0, nr_numbers):
  password_list += random.choice(numbers)

for letter in range(0, nr_letters):
  password_list += random.choice(letters)

for symbol in range(0, nr_symbols):
  password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list) # Did not work with the the variables inside the list previously built
print(password_list)

password=""
for char in password_list:
  password += char
print(password)
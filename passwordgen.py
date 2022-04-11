# PASSWORD GENERATOR PROJECT
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("WELCOME TO THE PASSWORD GENERATOR")
no_of_letters = int(input("How many letters your password should have?\n"))
no_of_numbers = int(input("How many numbers your password should have?\n"))
no_of_symbols = int(input("How many symbols your password should have?\n"))

password = ""
for char in range(1, no_of_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char

for num in range(1, no_of_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

for symbol in range(1,no_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol

print(password)

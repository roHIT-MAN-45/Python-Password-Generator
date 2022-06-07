#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("Enter number of letters for password : "))
num_numbers = int(input("Enter number of numbers for password : "))
num_symbols = int(input("Enter number of symbols for password : "))

pass_list = []
for char in range(1, num_letters + 1) : 
    # appending in list
    pass_list += random.choice(letters)


for num in range(1, num_numbers + 1) : 
    # appending in list
    pass_list += random.choice(numbers)

for symbol in range(1, num_symbols + 1) :
    # appending in list 
    pass_list += random.choice(symbols)

# Shuffling the list
random.shuffle(pass_list)

password = ""
for char in pass_list :
    password += char

print("Your strong Password is : " + password)
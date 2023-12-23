import secrets
import string

#defining variables
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation
allCharacters = upper_letters + lower_letters + digits + special_characters
password = ""

#taking inputs from user
password_length = int(input("Enter the desired length of password: "))
upper_min= int(input("Enter the minimum uppercase letters in the password: "))
lower_min= int(input("Enter the minimum lowercase letters in the password: "))
digits_min =int(input("Enter minimum number of digits in the password: ")) 
special_char_min= int(input("Enter the minimum number of special characters in the password: "))

#carrying out iteration for characters in password
for i in range(upper_min):
    password += "".join(secrets.choice(upper_letters))
    
for i in range(lower_min):
    password += "".join(secrets.choice(lower_letters))
    
for i in range(digits_min):
    password += "".join(secrets.choice(digits))
    
for i in range(special_char_min):
    password += "".join(secrets.choice(special_characters))
    
remaining = password_length - upper_min - lower_min - digits_min - special_char_min

for i in range(remaining):
    password += "".join(secrets.choice(allCharacters))
    
print("Your password is: "+ password)
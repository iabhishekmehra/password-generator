#i am gonna create a password generator. This password generator will generate a password with random characters.

import random

char = "abcdefghijklmnopqrstwxyz"
chars = char + char.upper()
password = ""

pass_len = int(input("What length of password would be good for you? : "))
spl_chars = input("would you like to add numbers and special character to your password? (yes/no) :")
if spl_chars == "yes":
    chars += "1234567890!@#$&*<>?"
while pass_len > len(password):
    password += random.choice(chars)
print(password)
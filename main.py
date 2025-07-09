import string as s
import random as r

letters = s.ascii_letters
digits = s.digits
symbols = s.punctuation

chars = letters + digits + symbols

length = int(input("Enter the desired password length: "))

password = "".join(r.choice(chars) for _ in range(length))

print("Your generated password:", password)

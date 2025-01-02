import random
import string

password_len = int(input("Write password length:"))
my_password = ""

for i in range(password_len):
    my_password += random.choice(string.ascii_letters)

print(f"Your new password is : {my_password}")
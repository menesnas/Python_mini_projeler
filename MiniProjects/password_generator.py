# RANDOM PASSWORD GENERATOR
"""
import random
import string

chars = []
passwordlist = []
def generate_password(length):
    chars.append(string.ascii_letters)
    chars.append(string.punctuation)
    chars.append(string.digits)
    passw = "".join(chars)
    len_a = len(passw)
    while (length > 0):
        len_a = len_a - 1
        i = random.randint(0,len_a)
        passwordlist.append(passw[i])
        length -= 1
    print(passwordlist)

lenn = int(input("Enter the length of password : "))
generate_password(lenn)
"""
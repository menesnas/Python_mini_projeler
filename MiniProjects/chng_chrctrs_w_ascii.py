#   this algorithm is written by beginner developer for exercise :)
"""
psswrd = input("enter password : ")
i = 0
print(psswrd)
listp = list(psswrd)
while(i < len(listp)):
    if ((ord(listp[i]) >= 65 and ord(listp[i]) <= 90)):
        listp[i] = str(chr(ord(listp[i]) + 32))
    elif (ord(listp[i]) >= 97 and ord(listp[i]) <= 122):
        listp[i] = str(chr(ord(listp[i]) - 32))
    else:
        pass
    i = i + 1
psswrd = "".join(listp)
print(psswrd)
"""

# ***********************************************************************
#   built-in function
"""
psswrd = input("enter password: ")
listp = list(psswrd)
for i in range(len(listp)):
    if 'A' <= listp[i] <= 'Z':
        listp[i] = listp[i].lower()
    elif 'a' <= listp[i] <= 'z':
        listp[i] = listp[i].upper()
psswrd = "".join(listp)
print(psswrd)
"""
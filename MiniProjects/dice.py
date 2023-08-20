"""
import random
import time 

i = 1
while True:
    zar1 = random.randint(1,6)
    zar2 = random.randint(1,6)
    if (zar1 == 6 and zar2 == 6):
        print("Zarlar {} kez atildi. \nzar-1 : {}\nzar-2 : {}".format(i,zar1,zar2))
        time.sleep(2)
        break
    print("Zarlar {} kez atildi. \nzar-1 : {}\nzar-2 : {}".format(i,zar1,zar2))
    i += 1
    time.sleep(1)

print("\n\n{}. denemede 6-6 geldi.\nzar-1 : {}\nzar-2 : {}".format(i,zar1,zar2))
"""
"""
import random
import sys

globalpi = 3.14

k = int(input("Enter the number of sides : "))

def circle():
    r = int(input("Enter the radius : "))
    print("\nCalculating...\n")
    result = 2 * globalpi * r
    print("Perimeter is : {0}".format(result))

class Shape:
    def __init__(self,snum):
        self.snum = snum
    
    def shape(self):
        nums = self.snum
        nums = nums - 1
        print("1)Random side lengths\n2)Input")
        choice = input("Choose : ")
        self.snum = self.snum - 1
        sides = [random.randint(1,10)]
        sides2 = []
        if (choice == "1"):
            while(self.snum > 0):
                sides.append(random.randint(1,10))
                self.snum = self.snum - 1
            res = sum(sides)
            print(sides)
            print("Perimeter is : {0}".format(res))
        elif (choice == "2"):
            i = 0
            while(nums >= 0):
                s = int(input("Side {0} : ".format(i)))
                i += 1
                nums -= 1
                sides2.append(s)
            res2 = sum(sides2)
            print(sides2)
            print("Perimeter is : {0}".format(res2))

if ((k < 3 and k > 0) or k < 0):
    print("Try again")
    sys.exit()
elif (k == 0):
    circle()
elif (k >= 3):
    nesne = Shape(k)
    nesne.shape()
"""
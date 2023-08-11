#   How many seconds have you lived until now ?

from datetime import *

birth = datetime.strptime(input("Your birth date --> (d.m.Y): "), "%d.%m.%Y")
second  = datetime.now() - birth
print("You survived {} seconds ".format(second.total_seconds()))
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
   print(number, "is greater than 5")
elif number == 0:
   print(number, "is 0")
else:
   print(number, "is less than 6 and not 0") 

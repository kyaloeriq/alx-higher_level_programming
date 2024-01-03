#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdgt = abs(number) % 10  # getting the last digit
sgn = '' if lstdgt >= 0 else '-'  # sign of the last digit
abslstdgt = abs(lstdgt)  # absolute value of last digit
if abslstdgt > 5:
    print(f"Last digit of {number} is {sgn}{abslstdgt} and is greater than 5")
elif abslstdgt == 0:
    print(f"Last digit of {number} is {sgn}{abslstdgt} and is 0")
else:
    print(f"Last digit of {number} is {sgn}{abslstdgt} and is less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdgt = abs(number) % 10  # getting the last digit

if number < 0:
    lstdgt *= -1  # for negative numbers, last digit also negative

if lstdgt > 5:
    print(f"Last digit of {number} is {lstdgt} and is greater than 5")
elif lstdgt == 0:
    print(f"Last digit of {number} is {lstdgt} and is 0")
else:
    print(f"Last digit of {number} is {lstdgt} and is less than 6 and not 0")

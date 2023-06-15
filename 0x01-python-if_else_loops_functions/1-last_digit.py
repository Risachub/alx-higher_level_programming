#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit1 = abs(number) % 10
if number < 0:
    digit1 = -digit1
print("Last digit of {} is {} and is ".format(number, digit1), end="")
if digit1 > 5:
    print("greater than 5")
elif digit1 == 0:
    print("0")
else:
    print("less than 6 and not 0")

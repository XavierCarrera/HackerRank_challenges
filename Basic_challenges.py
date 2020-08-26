# IF CHALLENGE

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n > 2 and n < 5:
        print("Not Weird")
    elif n % 2 == 0 and n > 6 and n < 20:
        print("Weird")
    else: 
        print("Not Weird")

# Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

# Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a//b)
    print(a/b)

# Square loop

if __name__ == '__main__':
    n = int(input())

    for i in range (0, n):
        print(i**2)

# Leap Year Function

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    return leap

year = int(input())

# Print function

if __name__ == '__main__':
    n = int(input())
    
    for i in range (1,n+1):
        print(i, end="")


        
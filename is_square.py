# Given an integer, determine if it's a square number


#My Solution:

def is_square(n): 
    if n < 0: return False
    elif n == 0: return True #i added this line because test case didn't work for 0 without this. Need to check why
    else:
        for i in range(n):
            square = i**2
            if n == square: return True
            elif n < square: return False


#Other Solutions:

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;


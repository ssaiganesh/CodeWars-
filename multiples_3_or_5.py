# Function that returns the sum of all the multiples of 3 or 5 below the number passed in.

#My Solution:
def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0:
            sum += i
            
        elif i % 5 == 0:
            sum += i
    return sum

#Recommended Solutions:
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
#Function to return missing number in a shuffled list

#My Solution 1: This was my first solution and it timed out
def find_missing_number(numbers):
    for i in range(1,(max(numbers)+1)):
        if i not in numbers:
            return i
        elif i == max(numbers):
            return i+1

#My Solution that worked
def  find_missing_number(numbers):
    
    if not numbers: n = 1
    else: n = sum(range(max(numbers)+1)) - sum(numbers)
    return n if n != 0 else (max(numbers) + 1)


#Recommended solution:
def find_missing_number(a):
    n = len(a) + 1
    return n * (n + 1) // 2 - sum(a)

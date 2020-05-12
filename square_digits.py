"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""

# My Solution:

def square_digits(num):
    digit_list = list(str(num).strip())
    answer_list= []
    for i in digit_list:
        answer_list.append(str(int(i)**2))
    answer = ''.join(answer_list)
    return int(answer)



#Other Solutions:

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)



def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
'''
Returns the average of two or more numbers.

Use sum() to sum all of the args provided, divide by len(args).'''
def average(*args):
    return sum(args, 0.0) / len(args)

print(average(*[1, 2, 3])) # 2.0
average(1, 2, 3) # 2.0

'''
Returns the average of a list, after mapping each element to a value using the provided function.

Use map() to map each element to the value returned by fn. 
Use sum() to sum all of the mapped values, divide by len(lst).
'''
def average_by(lst, fn=lambda x: x):
    return sum(map(fn, lst), 0.0) / len(lst)

print(average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])) # 5.0

'''
Clamps num within the inclusive range specified by the boundary values a and b.

If num falls within the range, return num. Otherwise, return the nearest number in the range.
'''
def clamp_number(num,a,b):
    return max(min(num, max(a,b)),min(a,b))

'''
Converts an angle from degrees to radians.

Use math.pi and the degrees to radians formula to convert the angle from degrees to radians.
'''
import math

def degrees_to_rads(deg):
    return (deg * math.pi) / 180.0
print(degrees_to_rads(180))

def rads_to_degrees(rad):
  return (rad * 180.0) / math.pi

'''
Converts a number to an array of digits.

Use map() combined with int on the string representation of n and return a list from the result.
'''
def digitize(n):
    return list(map(int, str(n)))
print(digitize(12345))

'''
Calculates the factorial of a number.

Use recursion. 
If num is less than or equal to 1, return 1. 
Otherwise, return the product of num and the factorial of num - 1. 
Throws an exception if num is a negative or a floating point number.
'''
def factorial(num):
    if not ((num >= 0) and (num % 1 == 0)):
        raise Exception(
            f"Number( {num} ) can't be floating point or negative ")
    return 1 if num == 0 else num * factorial(num - 1)

'''
Generates an array, containing the Fibonacci sequence, up until the nth term.

Starting with 0 and 1, use list.append() to add the sum of the last two numbers of the list to
    the end of the list, until the length of the list reaches n. 
    If n is less or equal to 0, return a list containing 0.
'''
def fibonacci(n):
    if n <= 0:
        return [0]
    sequence = [0, 1]
    while len(sequence) <= n:
        next = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next)
    
    return sequence

print(fibonacci(7))

'''
Calculates the greatest common divisor of a list of numbers.

Use reduce() and math.gcd over the given list.
'''
from functools import reduce
import math

def gcd(numbers):
    return reduce(math.gcd, numbers)
print(gcd([8,36,28]))

'''
Checks if the given number falls within the given range.

Use arithmetic comparison to check if the given number is in the specified range.
If the second parameter, end, is not specified, the range is considered to be from 0 to start.
'''
def in_range(n, start, end = 0):
    if end > start:
        start, end = end, start
    return start <= n <= end    

in_range(3, 2, 5); # True
in_range(3, 4); # True
in_range(2, 3, 5); # False
in_range(3, 2); # False


'''
Checks if the first numeric argument is divisible by the second one.

Use the modulo operator (%) to check if the remainder is equal to 0.
'''
def is_divisible(dividend, divisor):
    return dividend % divisor == 0

'''
Returns True if the given number is even, False otherwise.

Checks whether a number is odd or even using the modulo (%) operator. 
Returns True if the number is even, False if the number is odd.
'''
def is_even(num):
    return num % 2 == 0
def is_odd(num):
    return num % 2 != 0

'''
Returns the least common multiple of two or more numbers.

Define a function, spread, that uses either list.extend() or list.append() on each element in a list
 to flatten it. Use math.gcd() and lcm(x,y) = x * y / gcd(x,y) to determine the least common multiple.
'''
from functools import reduce
import math

def spread(lst):
    ret = []
    for item in lst:
        if isinstance(item, list):
            ret.extend(item)
        else:
            ret.append(item)
    return ret

def lcm(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _lcm(x, y):
        return int(x * y / math.gcd(x, y))
    
    return reduce(lambda x, y: _lcm(x, y), numbers)

print(lcm(12, 7)) #84
print(lcm([1, 3, 4], 5)) #60

'''
Returns the maximum value of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use max() to return the maximum value.
'''
def max_by(lst, fn = lambda x: x):
    return max(map(fn, lst))

print(max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))

'''
Finds the median of a list of numbers.

Sort the numbers of the list using list.sort() and find the median, 
which is either the middle element of the list if the list length is odd or
     the average of the two middle elements if the list length is even.
'''
def median(lst):
    list.sort(lst) # 原地排序
    list_length = len(lst)
    if list_length % 2 == 0:
        return (lst[int(list_length / 2) - 1] + lst[int(list_length / 2)]) / 2
    else :
        return lst[int(list_length / 2)]

print(median([1,2,3]))
print(median([1,2,3, 4]))

'''
Returns the sum of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use sum() to return the sum of the values.
'''
def sum_by(lst, fn: lambda x: x):
    return sum(map(fn, lst))


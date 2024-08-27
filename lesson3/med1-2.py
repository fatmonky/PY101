"""
original code:
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
"""

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0: #checks that divisor is a factor for number i.e. no remainder.
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(10)) #expect 10, 5,2, 1
print(factors(12)) #expect 12, 6,4, 3, 2, 1

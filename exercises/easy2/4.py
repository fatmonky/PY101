def square(num):
    multiply(num, num)

def multiply(num1, num2):
    return num1 * num2 

def power_to_n(num, n):
    return_val = 1
    while n > 0:
        return_val = multiply(return_val, num)
        n -= 1
    return return_val

print(square(5) == 25)   # True
print(square(-8) == 64)  # True
print(square(5))
print(square(-8))
print(power_to_n(2, 3))
print(power_to_n(2, 4))
print(power_to_n(2, 3) == 8)   # True
print(power_to_n(2, 4) == 16)   # True


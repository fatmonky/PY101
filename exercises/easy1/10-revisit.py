def multisum(num):
    index = 1
    total = 0
    while index < num:
        index += 1
        if index % 3 == 0 or index % 5 == 0:
            total += index
    return total

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(20) == 98)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

# model answer:
# very elegant use of for-loop and range here, in line 24.
def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(max_value):
    total_sum = 0
    for number in range(1, max_value + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            total_sum += number
    return total_sum

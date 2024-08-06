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

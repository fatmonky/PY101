def negative(num):
    if num > 0:
        return num * -1
    else:
        return num

# tests:
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

# model answer:
def negative(number):
    return -abs(number)

def stringy(num):
    new_string = ""
    for char in range(num):
        if char % 2 == 0:
            new_string += "1"
        else:
            new_string += "0"
    return new_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

# model answer uses ternary expression:
def stringy(size):
    result = ""
    for idx in range(size):
        digit = '1' if idx % 2 == 0 else '0' #Ternary expression here. Elegant!
        result += digit

    return result

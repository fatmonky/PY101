def xor(arg1, arg2):
    if arg1 and (arg2 == False):
        return True
    elif arg2 and (arg1 == False):
        return True
    elif arg1 == True and arg2 == True:
        return False
    else:
        return False


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

# further exploration
# stair lights with switches at the top and bottom. 
# also, air-lock, or water-lock, which allows either (but not both) door to be open.
# short-circuit evaluation does not make sense in xor, as you NEED to evaluate the other value to see if it's the same as the first value. 

# model answer:
def xor(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))

def center_of(string):
    string_length = len(string)
    if string_length % 2 == 0:
        return string[string_length // 2 - 1] + string[(string_length // 2)]
    else:
        return string[string_length // 2]

# tests
print(center_of('I Love Python!!!'))
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True

# model answer:


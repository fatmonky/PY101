def crunch(string):
    new_string = ""
    char_mem = ''
    for char in string:
        if char in char_mem:
            pass
        else:
            new_string += char
            char_mem = char
    return new_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

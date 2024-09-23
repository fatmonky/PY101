"""
Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

ExamplesCopy Code
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
"""
#take string argument
# set new_string_list
# set old_char to store previous char
# iterate through string, and check if each character is old_char
#   if yes, move onto next_char
#   if no, add character to new_string
#   at end of string, return new_string.

def crunch(string):
    new_string = ""
    old_char = ''
    for char in string:
        if char == old_char: # uses old_char to track an old char
            pass
        else:
            new_string += char
        old_char = char
    return new_string


# tests
# These examples should all print True
print(crunch('4444abcabccba'))
print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

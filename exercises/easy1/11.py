# write a function that determines and returns the UTF-16 string value of a string passed in as an argument.

#7 Aug 24
# pseudocode
"""
START define utf16_value(str)
# Check if str is valid
IF type(str) != string
THEN return None
ELSE
    SET total_char_value = 0
    SET str_list = list(str) #converts string to list of characters
    FOR char in str_list
        total_char_value += ord(char)
    return total_char_value
"""

'''
def utf16_value(string_input):
    """calculates sum of UTF-16 string_inputing value of string_inputing"""
    if type(string_input) != str:
        return None
    total_char_value = 0
    string_input_list = list(string_input)
    for char in string_input_list:
        total_char_value += ord(char)
    return total_char_value
'''
'''
# model answer:
def utf16_value(string):
    sum_ = 0
    for char in string:
        sum_ += ord(char)
    return sum_
'''
"""comments: this is simpler, and the same vein. However, this doesn\'t do input validation e.g. if there\'s a non-string input, it\'s unclear if this works?"""

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)
print(utf16_value(40) == None)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)



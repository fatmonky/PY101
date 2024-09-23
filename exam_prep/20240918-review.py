"""
# easy3/1
def repeat(string, num):
    for _ in range(num):
        print(string)

repeat("hello", 3)
repeat("hello world", 3)

"""
def crunch(string):
    """
    create new list.
    iterate through string
        for each char, to check if char in new_list
            if not in new_list, to append
    return new_list.join()
    """
    new_list = ""
    old_char = ''
    for char in string:
        if char in old_char:
            pass
        else:
            new_list += char
        old_char = char
    return new_list

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee')) 
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

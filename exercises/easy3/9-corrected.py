"""
def clean_up(string):
    new_string = ""
    for char in string:
        # if char is not alpha, and char + 1 is not alpha, 
        # char = " "
        # skip to first alphabetical
        if char.isalpha():
            new_string += char
        else:
            char = " "
        new_string += char
    return new_string
"""
# correction:
def clean_up(string):
    new_string = ""

    for idx, char in enumerate(string):
        if char.isalpha() and char.isascii():
            new_string += char
        elif idx == 0 or new_string[-1] != " ":
            new_string += " "
    return new_string

print(clean_up("---what's my +*& line?"))
print(clean_up("---what's my +*& line?") == " what s my line ")
# True

# debrief on personal attempt: can't solve this, as I was introducing too many spaces.

# model answer: includes a clause that checks if the new_string's last space was NOT an empty space, and to only concatenate a space only if the last entry was not an empty space
# model answer also uses enumerate on string, to introduce an index. Very elegant! 



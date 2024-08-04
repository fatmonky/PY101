def short_long_short(str1, str2):
    if len(str1) > len(str2):
        return str2 + str1 + str2
    elif len(str1) < len(str2):
        return str1 + str2 + str1

# tests
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

#model answer:
# model answer doesn't spell out elif, just else. This is due to the base assumption of the problem ("You may assume that the strings are of different lengths") i.e. there is no equals.

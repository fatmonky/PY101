def twice(num):
    # check if num is a doublenumber
    # if yes, return num
    # if no, return num * 2
    if check_double(num):
        return num
    else:
        return num * 2

    """
def check_double(num):
    convert num to string, and check if length % 2 == 0
    #   if no, then return False
    # if yes, then next check:
    #   for char in num_string:
    #   rfind if char exists in string
        # if rfind = -1, return False
        if .rfind(char) != 1:
        if .rfind(char) - .find(char) %2 == 1
        return True
        else
        return False
    num_string = str(num)
    if len(num_string) % 2 != 0:
        return False
    else:
        for char in num_string:
            if num_string.rfind(char) == -1:
                return False
            if (num_string.rfind(char) - num_string.find(char)) % 2 == 1:
                return True
            else:
                return False
    """

# correction, using model answer logic: this is very brilliant, as it uses Python string slicing to make comparison between left and right of a numerical string a breeze!
def check_double(num):
    num_string = str(num)
    center_idx = len(num_string) // 2
    left_number = num_string[:center_idx]
    right_number = num_string[center_idx:]
    return left_number == right_number

# tests
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True # mine is False
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True #mine is False

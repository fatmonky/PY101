# 1. how to calculate the year as input and return the century.
# 2. how to append the right 'st', 'nd' etc. for the century.
"""
def century(year):
    CENTURY = 99
    if 0 <= year < 101:
        century_number = 1
    elif 101 <= year < 201:
        century_number = 2
    else:
        century_number = year // CENTURY + 1

    return f"{century_number}th"
"""

# correction:
def century(year):
    century_number = year // 100 + 1
    if year % 100 == 0:
        century_number -= 1
    return f"{century_number}{suffix(century_number)}"

def suffix(century_number):
    last_two = century_number % 100
    last_digit = century_number % 10

    match last_two:
        case 11 | 12 | 13:
            return "th"

    match last_digit:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"


# tests
print(century(2000))
print(century(2001))
print(century(1965))
print(century(256))
print(century(5))   
print(century(10103))
print(century(1052))
print(century(1127))
print(century(11201))

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

# correction: missed the observation of the pattern, that the century = year // 100 + 1, unless it is a multiple of 100. 

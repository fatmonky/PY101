# didn't use date-time, and hard-coded 2024.

# correction:

from datetime import datetime #see solution notes on importing modules and classes.

age = input("What is your age? ")
retirement_age = input("At what age would you like to retire? ")

number_of_years_left = int(retirement_age) - int(age)
current_year = datetime.now().year #correction
retirement_year = current_year + number_of_years_left

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You only have {number_of_years_left} years of work to go!")

# TODO: write code
# TODO: check for edge cases
# TODO: pylint code

"""
Calculator for monthly mortgage payments
"""

def prompt(message):
    print(f"=> {message}")

# SET monthly_mortgage_calculation function:
    # IF INTEREST_MONTHLY == 0
        # return LOAN_AMOUNT / LOAN_DURATION_MONTHLY
    # ELSE
        # return LOAN_AMOUNT * (INTEREST_MONTHLY / (1 - (1+ INTEREST_MONTHLY) ** (- LOANDURATION_MONTHLY)))
def monthly_mortgage_calculation(monthly_int, loan_amt, loan_dur):
    if monthly_int == 0:
        return loan_amt / loan_dur
    else:
        return loan_amt * (monthly_int / (1 - (1 + monthly_int) ** (- loan_dur)))


# START Program: import json
# SET program_loop = True

program_loop = True

# WHILE program_loop:
while program_loop:
# PRINT "Welcome to the monthly mortgage calculator."
    prompt("Welcome to the monthly mortgage calculator.")
# PRINT "Please enter your loan amount (we are assuming dollars)"
    prompt("Please enter your loan amount (we are assuming dollars): ")
# GET loan amount from the user
# SET LOAN_AMOUNT
    LOAN_AMOUNT = float(input())

# PRINT "Please enter your annual interest in percentages e.g. if it's 4.5%, key in '4.5'"
    prompt("Please enter your annual interest in percentages e.g. if it's 4.5%, key in '4.5': ")
# GET annual interest (in float) from user
# SET ANNUAL_INTEREST
    ANNUAL_INTEREST = float(input())
# PRINT "Please enter your loan duration in years (note: you may enter half years e.g. 2.5 years)"
    prompt("Please enter your loan duration in years ")
    prompt("(note: you may enter half years e.g. 2.5 years): ")
# GET loan duration (in float years) from user
# SET LOAN_DURATION_YEARS
    LOAN_DURATION_YEARS = float(input())

# SET INTEREST_MONTHLY = (ANNUAL_INTEREST / 12) / 100
    INTEREST_MONTHLY = (ANNUAL_INTEREST / 12) / 100
# SET LOAN_DURATION_MONTHLY = LOAN_DURATION_YEARS * 12
    LOAN_DURATION_MONTHLY = LOAN_DURATION_YEARS * 12
# PRINT f"Your monthly mortgage payment is ${monthly_mortgage_calculation()}.:..2f}."
    prompt(f"Your monthly mortgage payment is:") 
    prompt(f"${monthly_mortgage_calculation(INTEREST_MONTHLY, LOAN_AMOUNT, LOAN_DURATION_MONTHLY):.2f}.")
# PRINT "Would you like to calculate another mortgage? Y/n"
    prompt("Would you like to calculate another mortgage? Y/n")
# GET another_calc from user
# SET another_calc
    another_calc = input()
    # IF another_calc not in ['Y', 'y', 'N', 'n']:
    # break
    if another_calc not in ['Y', 'y']: 
        break
# PRINT "Thank you for using the mortgage calculator! Seeya next time!"
prompt("Thank you for using the mortgage calculator! Seeya next time!")

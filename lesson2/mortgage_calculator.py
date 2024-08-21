# TODO: remove pseudocode (done)
# TODO: move all messages to JSON file.
# TODO: refactor code for clarity
# TODO: check for edge cases
# TODO: pylint code


"""
Calculator for monthly mortgage payments
"""

import os
import json

def prompt(message):
    print(f"=> {message}")

def monthly_mortgage_calculation(monthly_int, loan_amt, loan_dur):
    if monthly_int == 0:
        return loan_amt / loan_dur
    else:
        return loan_amt * (monthly_int / (1 - (1 + monthly_int)
                                          ** (- loan_dur)))

program_loop = True

prompt("Welcome to the monthly mortgage calculator.")
while program_loop:
    prompt("Please enter your loan amount (we are assuming dollars): ")
    LOAN_AMOUNT = float(input())

    prompt("Please enter your annual interest in percentages e.g. if it's 4.5%, key in '4.5': ")
    ANNUAL_INTEREST = float(input())
    prompt("Please enter your loan duration in years ")
    prompt("(note: you may enter half years e.g. 2.5 years): ")
    LOAN_DURATION_YEARS = float(input())

    INTEREST_MONTHLY = (ANNUAL_INTEREST / 12) / 100
    LOAN_DURATION_MONTHLY = LOAN_DURATION_YEARS * 12
    prompt(f"Your monthly mortgage payment is:") 
    prompt(f"${monthly_mortgage_calculation(INTEREST_MONTHLY, LOAN_AMOUNT, LOAN_DURATION_MONTHLY):.2f}.")
    prompt("Would you like to calculate another mortgage? Y/n")
    another_calc = input()
    if another_calc not in ['Y', 'y']:
        break
    os.system('clear')
prompt("Thank you for using the mortgage calculator! Seeya next time!")

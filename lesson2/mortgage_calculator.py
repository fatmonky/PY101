# TODO: remove pseudocode (done)
# TODO: move all messages to JSON file.(done)
# TODO: refactor code for clarity: move functionality to functions, 
# TODO: check for edge cases: include helpers to check for valid input
# TODO: pylint code


"""
Calculator for monthly mortgage payments
"""

import os
import json

with open('mortgage_messages.json','r') as file:
    msg_data = json.load(file)

def prompt(message):
    print(f"=> {message}")

def clear_screen():
    os.system('clear')

def monthly_mortgage_calculation(monthly_int, loan_amt, loan_dur):
    if monthly_int == 0:
        return loan_amt / loan_dur
    else:
        return loan_amt * (monthly_int / (1 - (1 + monthly_int)
                                          ** (- loan_dur)))

def valid_number_check(num):
    try:
        float_num = float(num)
    except ValueError:
        return False
    if num.isdigit():
        return True
    return isinstance(float_num, float)

def number_validation(num):
    if valid_number_check(num) is False:
        prompt(msg_data["invalid_number"])


def get_loan_amount():
    prompt(msg_data["welcome"])
    while True:
        prompt(msg_data["loan_amount"])
        LOAN_AMOUNT = input()
        number_validation(LOAN_AMOUNT)
        if valid_number_check(LOAN_AMOUNT):
            break
    return float(LOAN_AMOUNT)

def get_annual_interest():
    while True:
        prompt(msg_data["annual_interest"])
        ANNUAL_INTEREST = input()
        number_validation(ANNUAL_INTEREST)
        if valid_number_check(ANNUAL_INTEREST):
           break 
    return float(ANNUAL_INTEREST)

def get_loan_duration_years():
    while True:
        prompt(msg_data["loan_duration_years"])
        prompt(msg_data["loan_duration_years_2"])
        LOAN_DURATION_YEARS = input()
        number_validation(LOAN_DURATION_YEARS)
        if valid_number_check(LOAN_DURATION_YEARS):
            break
    return float(LOAN_DURATION_YEARS)

def display_results():
    prompt(msg_data["monthly_mortgage_payment"]) 
    prompt(f"${monthly_mortgage_calculation(INTEREST_MONTHLY, LOAN_AMOUNT, LOAN_DURATION_MONTHLY):.2f}.")


def main():

    while True:
        clear_screen()
        LOAN_AMOUNT = get_loan_amount()

        ANNUAL_INTEREST = get_annual_interest()

        LOAN_DURATION_YEARS = get_loan_duration_years()

        INTEREST_MONTHLY = (ANNUAL_INTEREST / 12) / 100
        LOAN_DURATION_MONTHLY = LOAN_DURATION_YEARS * 12
        display_results()
        prompt(msg_data["calculate_another?"])
        another_calc = input()
        if another_calc not in msg_data["calculation_choices"]:
            break
    prompt(msg_data["farewell"])

main()

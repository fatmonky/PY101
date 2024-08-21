# TODO: remove pseudocode (done)
# TODO: move all messages to JSON file.(done)
# TODO: refactor code for clarity: move functionality to functions,  (mostly done)
# TODO: check for edge cases: include helpers to check for valid input (partially done)
# TODO: troubleshoot calculate_again function, and how that fits into the main program loop.
# TODO: pylint code


"""
Calculator for monthly mortgage payments
"""

import os
import json
import pdb #remove before prod

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
        LOAN_AMOUNT = input().strip()
        number_validation(LOAN_AMOUNT)
        if valid_number_check(LOAN_AMOUNT):
            break
    return float(LOAN_AMOUNT)

def get_annual_interest():
    while True:
        prompt(msg_data["annual_interest"])
        ANNUAL_INTEREST = input().strip()
        number_validation(ANNUAL_INTEREST)
        if valid_number_check(ANNUAL_INTEREST):
           break 
    return float(ANNUAL_INTEREST)

def get_loan_duration_years():
    while True:
        prompt(msg_data["loan_duration_years"])
        prompt(msg_data["loan_duration_years_2"])
        LOAN_DURATION_YEARS = input().strip()
        number_validation(LOAN_DURATION_YEARS)
        if valid_number_check(LOAN_DURATION_YEARS):
            break
    return float(LOAN_DURATION_YEARS)

def display_results(results):
    prompt(msg_data["monthly_mortgage_payment"]) 
    prompt(f"${results:.2f}.")

def calculate_again():
    while True:
        prompt(msg_data["calculate_another?"])
        another_calc = input().strip()
        if another_calc not in msg_data["valid_calculation_choices"]:
            prompt(msg_data["invalid_choice"])
        if another_calc in msg_data["valid_calculation_choices"]:
            break
    if another_calc in msg_data["calculation_choices"]:
        return True
    return False

def main():

    while True:
        clear_screen()
        LOAN_AMOUNT = get_loan_amount()
        ANNUAL_INTEREST = get_annual_interest()
        LOAN_DURATION_YEARS = get_loan_duration_years()
        INTEREST_MONTHLY = (ANNUAL_INTEREST / 12) / 100
        LOAN_DURATION_MONTHLY = LOAN_DURATION_YEARS * 12
        results = monthly_mortgage_calculation(INTEREST_MONTHLY, LOAN_AMOUNT, LOAN_DURATION_MONTHLY)
        display_results(results)
        repeat_calc = calculate_again()
        if repeat_calc is False:
            break
    clear_screen()
    prompt(msg_data["farewell"])

main()

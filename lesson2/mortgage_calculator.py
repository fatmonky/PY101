"""
Calculator for monthly mortgage payments
"""

import os
import json

with open('mortgage_messages.json','r') as file:
    MSG_DATA = json.load(file)

def prompt(message):
    print(f"=> {message}")

def clear_screen():
    os.system('clear')

def monthly_mortgage_calculation(monthly_int, loan_amt, loan_dur):
    if monthly_int == 0:
        try:
            loan_amt / loan_dur
        except ZeroDivisionError:
            prompt(MSG_DATA["zero_error"])
            return 0
        return loan_amt / loan_dur
    if loan_dur == 0:
        return loan_amt
    return loan_amt * (monthly_int / (1 - (1 + monthly_int)
                                          ** (- loan_dur)))

def try_float_num(num):
    try:
        float_num = float(num)
    except ValueError:
        return False
    return float_num

def not_negative(num, message):
    float_num = try_float_num(num)
    if float_num < 0:
        prompt(MSG_DATA[message])
        return False
    if float_num is False:
        return False
    if valid_number_check(num):
        return True
    return True

def valid_number_check(num):
    float_num = try_float_num(num)
    if num.isdigit():
        return True
    return isinstance(float_num, float)

def display_invalid_number(num):
    if valid_number_check(num) is False:
        prompt(MSG_DATA["invalid_number"])

def valid_loan_check(loan_amount):
    return not_negative(loan_amount, "invalid_loan")

def get_loan_amount():
    prompt(MSG_DATA["welcome"])
    while True:
        prompt(MSG_DATA["loan_amount"])
        loan_amount = input().strip()
        display_invalid_number(loan_amount)
        if valid_loan_check(loan_amount):
            break
    return float(loan_amount)

def valid_interest_check(annual_interest):
    return not_negative(annual_interest, "invalid_interest")

def get_annual_interest():
    while True:
        prompt(MSG_DATA["annual_interest"])
        annual_interest = input().strip()
        display_invalid_number(annual_interest)
        if valid_interest_check(annual_interest):
            break
    return float(annual_interest)

def valid_duration_check(duration):
    return not_negative(duration, "invalid_duration")

def get_loan_duration_years():
    while True:
        prompt(MSG_DATA["loan_duration_years"])
        prompt(MSG_DATA["loan_duration_years_2"])
        loan_duration_years = input().strip()
        display_invalid_number(loan_duration_years)
        if valid_duration_check(loan_duration_years):
            break
    return float(loan_duration_years)

def display_results(results, loan_amount,
                    annual_interest,
                    loan_duration_years):
    prompt(MSG_DATA["your_amount"])
    prompt(f"${loan_amount:_.0f}")
    prompt(MSG_DATA["your_interest"])
    prompt(f"{annual_interest:.2f}%")
    prompt(MSG_DATA["your_duration"])
    prompt(f"{loan_duration_years:.1f} years")
    print("\n")
    prompt(MSG_DATA["monthly_mortgage_payment"])
    prompt(f"${results:.2f}")
    print("\n")

def get_calculation_again():
    while True:
        prompt(MSG_DATA["calculate_another?"])
        another_calc = input().strip()
        if another_calc not in MSG_DATA["valid_calculation_choices"]:
            prompt(MSG_DATA["invalid_choice"])
        if another_calc in MSG_DATA["valid_calculation_choices"]:
            break
    if another_calc in MSG_DATA["calculation_choices"]:
        return True
    return False

def display_farewell():
    prompt(MSG_DATA["farewell"])


def main():
    while True:
        clear_screen()
        loan_amount = get_loan_amount()
        annual_interest = get_annual_interest()
        loan_duration_years = get_loan_duration_years()
        interest_monthly = (annual_interest / 12) / 100
        loan_duration_monthly = loan_duration_years * 12
        results = monthly_mortgage_calculation(
                interest_monthly, loan_amount,
                loan_duration_monthly)
        clear_screen()
        display_results(results, loan_amount,
                        annual_interest,
                        loan_duration_years)
        if not get_calculation_again():
            break
    clear_screen()
    display_farewell()

main()

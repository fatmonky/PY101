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
        loan_amount = input().strip()
        number_validation(loan_amount)
        if valid_number_check(loan_amount):
            break
    return float(loan_amount)

def get_annual_interest():
    while True:
        prompt(msg_data["annual_interest"])
        annual_interest = input().strip()
        number_validation(annual_interest)
        if valid_number_check(annual_interest):
            break
    return float(annual_interest)

def get_loan_duration_years():
    while True:
        prompt(msg_data["loan_duration_years"])
        prompt(msg_data["loan_duration_years_2"])
        loan_duration_years = input().strip()
        number_validation(loan_duration_years)
        if valid_number_check(loan_duration_years):
            break
    return float(loan_duration_years)

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
        loan_amount = get_loan_amount()
        annual_interest = get_annual_interest()
        loan_duration_years = get_loan_duration_years()
        interest_monthly = (annual_interest / 12) / 100
        loan_duration_monthly = loan_duration_years * 12
        results = monthly_mortgage_calculation(
                interest_monthly, loan_amount,
                loan_duration_monthly)
        display_results(results)
        repeat_calc = calculate_again()
        if repeat_calc is False:
            break
    clear_screen()
    prompt(msg_data["farewell"])

main()

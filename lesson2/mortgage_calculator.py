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

while True:
    clear_screen()
    prompt(msg_data["welcome"])
    prompt(msg_data["loan_amount"])
    LOAN_AMOUNT = float(input())

    prompt(msg_data["annual_interest"])
    ANNUAL_INTEREST = float(input())
    prompt(msg_data["loan_duration_years"])
    prompt(msg_data["loan_duration_years_2"])
    LOAN_DURATION_YEARS = float(input())

    INTEREST_MONTHLY = (ANNUAL_INTEREST / 12) / 100
    LOAN_DURATION_MONTHLY = LOAN_DURATION_YEARS * 12
    prompt(msg_data["monthly_mortgage_payment"]) 
    prompt(f"${monthly_mortgage_calculation(INTEREST_MONTHLY, LOAN_AMOUNT, LOAN_DURATION_MONTHLY):.2f}.")
    prompt(msg_data["calculate_another?"])
    another_calc = input()
    if another_calc not in msg_data["calculation_choices"]:
        break
prompt(msg_data["farewell"])

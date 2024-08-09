"""
Refactored Calculator, 7 Aug 2024
930am: my first try without reading the walk-through.
4pm: revisions after reading walk-through don't work!
The use of try-except is interesting, but the use of int(num) doesn't work.
427pm: linted using pylint: code looks AMAZING... all in neat functions!

9 Aug 24 1113am: linted using pylint again. Now adding JSON functionality.
1137am: added all messages into calculator_messages.json file, and 
program works. Needed the hint!
1229pm: completed Calculator bonuses.

"""

import json

with open('calculator_messages.json', 'r') as file:
    msg_data = json.load(file)

def prompt(message):
    print(f"=> {message}")

def is_valid_number(num):
    return num.isdigit() or isinstance(float(num), float)

def is_valid_operator(op):
    return op.lower() in ['a', 's' ,'m' , 'd']

def invalid_language_check(lang):
    while lang not in ['e', 'E', 'f', 'F']:
        prompt(msg_data["invalid_language"])
        lang = input()
    if lang in ('f', 'F'):
        lang = msg_data['fr']
    else:
        lang = msg_data['en']
    return lang

def invalid_number_check(num):
    while is_valid_number(num) is False:
        prompt(lg["invalid_number"])
        num = input()
    return num

def invalid_operator_check(op):
    while is_valid_operator(op) is False:
        prompt(lg["invalid_operator"])
        op = input()
    return op

def invalid_wish_check(choice):
    while choice not in ['Y', 'y', 'N', 'n']:
        prompt(lg["invalid_wish"])
        choice = input()
    return choice

# perform calculation, using match-case, and display the result.
def calculation(numb1, numb2):
    match operator.lower():
        case 'a':
            return int(numb1 + numb2)
        case 's':
            return int(numb1 - numb2)
        case 'm':
            return int(numb1 * numb2)
        case 'd':
            return numb1 / numb2

prompt(msg_data["language"])
lg = input()
lg = invalid_language_check(lg)

calculate = True
prompt(lg["welcome"])

while calculate:
    prompt(lg["first_number"])
    num1 = input()
    num1 = invalid_number_check(num1)

    prompt(lg["second_number"])
    num2 = input()
    num2 = invalid_number_check(num2)

    prompt(lg["operation_type"])
    operator = input()
    operator = invalid_operator_check(operator)

    prompt(lg["result"])
    print(f"=>    {calculation(float(num1),float(num2)):.2f}.")

    prompt(lg["another_calculation"])
    user_wishes = input()
    user_wishes = invalid_wish_check(user_wishes)
    if user_wishes not in ['Y', 'y']:
        calculate = False

prompt(lg["thank_you"])

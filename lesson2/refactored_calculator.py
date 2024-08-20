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

14 Aug 24 954am: 
    TODO: address divide by zero error
    TODO: clear screen

20 Aug 453pm: completed incorporating Brandi's feedback! 

"""

import json
import os
import time

with open('calculator_messages.json', 'r') as file:
    msg_data = json.load(file)

def clear_screen():
    os.system('clear')

def choose_language():
    clear_screen()
    prompt(msg_data["language"])
    lang = input().strip()
    lang = invalid_language_check(lang)
    return lang

def prompt(message):
    print(f"=> {message}")

def is_valid_number(num):
    try:
        float_num = float(num)
    except ValueError:
        return False
    if num.isdigit():
        return True
    if isinstance(float_num, float):
        return True
    else:
        return False

def enter_number(message, lang):
    prompt(lang[message])
    num = input().strip()
    num = invalid_number_check(num, lang)
    return num

def is_valid_operator(op):
    return op.lower() in msg_data["valid_operators"]

def invalid_language_check(lang):
    while lang not in msg_data["valid_languages"]:
        prompt(msg_data["invalid_language"])
        lang = input().strip()
    if lang in ('f', 'F'):
        lang = msg_data['fr']
    else:
        lang = msg_data['en']
    return lang

def invalid_number_check(num, lang):
    while is_valid_number(num) is False:
        prompt(lang["invalid_number"])
        num = input().strip()
    return num

def invalid_operator_check(op, lang):
    while is_valid_operator(op) is False:
        prompt(lang["invalid_operator"])
        op = input().strip()
    return op

def invalid_wish_check(choice, lang):
    while choice not in lang["valid_wishes"]:
        prompt(lang["invalid_wish"])
        choice = input().strip()
    return choice

def operator_choice(lang):
    prompt(lang["operation_type"])
    operator = input().strip()
    operator = invalid_operator_check(operator, lang)
    return operator

# perform calculation, using match-case, and display the result.
def calculation(numb1, numb2, operator):
    numb1 = float(numb1)
    numb2 = float(numb2)
    match operator.lower():
        case 'a':
            return numb1 + numb2
        case 's':
            return numb1 - numb2
        case 'm':
            return numb1 * numb2
        case 'd':
            try:
                numb1 / numb2
            except ZeroDivisionError:
                return 'e'
            return numb1 / numb2

def display_result(numb1, numb2, operator, lang):
    prompt(lang["result"])
    print(f"=>    {calculation(float(numb1),float(numb2),operator):.2f}")


def calculate_again(lang):
    prompt(lang["another_calculation"])
    user_wishes = input().strip()
    user_wishes = invalid_wish_check(user_wishes, lang)
    return user_wishes


def main():
    lang = choose_language()
    calculate = True
    prompt(lang["welcome"])
    time.sleep(0.5)

    while calculate:
        clear_screen()

        num1 = enter_number("first_number", lang)
        num2 = enter_number("second_number", lang)
        operator = operator_choice(lang)

        if calculation(num1, num2, operator) == 'e':
            prompt(lang["divide_zero"])
            time.sleep(2)
            continue
        display_result(num1, num2, operator, lang)
        user_wishes = calculate_again(lang)
        if user_wishes not in lang["calc_again"]:
            calculate = False
        clear_screen()

    prompt(lang["thank_you"])

main()

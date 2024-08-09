"""
Refactored Calculator, 7 Aug 2024
930am: my first try without reading the walk-through.
4pm: revisions after reading walk-through don't work!
The use of try-except is interesting, but the use of int(num) doesn't work.
427pm: linted using pylint: code looks AMAZING... all in neat functions!
"""

def prompt(message):
    print(f"=> {message}")

def is_valid_number(num):
    return num.isdigit()

def is_valid_operator(op):
    return op.lower() in ['a', 's' ,'m' , 'd']

def invalid_number_check(num):
    while is_valid_number(num) is False:
        prompt("I'm sorry, that's not a valid number.")
        prompt("Please key in a valid number: ")
        num = input()
    return num

def invalid_operator_check(op):
    while is_valid_operator(op) is False:
        prompt("I'm sorry, that's not a valid operator.")
        prompt("Please key in a valid operator: ")
        prompt("Type\n'a' to add;\n's' to substract; \
               \n'm' to multiply;\n'd' to divide.\n")
        op = input()
    return op

def invalid_wish_check(choice):
    while choice not in ['Y', 'y', 'N', 'n']:
        prompt("I'm sorry,that's not a valid choice.")
        prompt("Please key in Y/n: ")
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

calculate = True
prompt("Welcome to the Calculator!")

while calculate:
    prompt("Enter the first number: ")
    num1 = input()
    num1 = invalid_number_check(num1)

    prompt("Enter the second number: ")
    num2 = input()
    num2 = invalid_number_check(num2)

    prompt("""What type of operation will you like to perform? Type
'a' to add;\n's' to substract;\n'm' to multiply;\n'd' to divide.\n""")
    operator = input()
    operator = invalid_operator_check(operator)

    print(f"""=> The result of your calculation is:
    =>    {calculation(float(num1),float(num2)):.2f}.""")

    prompt("Would you like to do another calculation? Y/n")
    user_wishes = input()
    user_wishes = invalid_wish_check(user_wishes)
    if user_wishes not in ['Y', 'y']:
        calculate = False

prompt("Thank you for using the calculator! See you next time!")

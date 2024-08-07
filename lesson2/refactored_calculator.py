# 7 Aug 2024, my first try without reading the walk-through, just the flowchart:

def prompt(message):
    print(f"=> {message}")

def is_valid_number(num):
    if num.isdigit():
        return True
    else:
        return False

def is_valid_operator(op):
    if op.lower() in ['a', 's' ,'m' , 'd']:
        return True
    else:
        return False

def invalid_number_check(num):
    while is_valid_number(num) == False:
        prompt("I'm sorry, that's not a valid number. Please key in a valid number: ")
        num = input()
    return num

def invalid_operator_check(op):
    while is_valid_operator(op) == False:
        prompt("I'm sorry, that's not a valid operator. Please key in a valid operator: ")
        prompt("Type\n'a' to add;\n's' to substract;\n'm' to multiply;\n'd' to divide.\n")
        op = input()
    return op

# perform calculation, using match-case, and display the result.
def calculation(num1, num2):
    match operator.lower():
        case 'a':
            return int(num1 + num2)
        case 's':
            return int(num1 - num2)
        case 'm':
            return int(num1 * num2)
        case 'd':
            return (num1 / num2)

prompt("Welcome to the Calculator!")
prompt("Enter the first number: ")
num1 = input()
num1 = invalid_number_check(num1)

prompt("Enter the second number: ")
num2 = input()
num2 = invalid_number_check(num2)

prompt("What type of operation will you like to perform? Type\n'a' to add;\n's' to substract;\n'm' to multiply;\n'd' to divide.\n")
operator = input()
operator = invalid_operator_check(operator)

print(f"The result of your calculation is {calculation(float(num1),float(num2)):.2f}.")

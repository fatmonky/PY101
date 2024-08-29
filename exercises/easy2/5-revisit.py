def prompt(message):
    print(f"=>{message}")

prompt("Enter the first number:")
first_num = float(input())

prompt("Enter the second number:")
second_num = float(input())

prompt(f"{first_num} + {second_num} = {first_num + second_num}")
prompt(f"{first_num} - {second_num} = {first_num - second_num}")
prompt(f"{first_num} * {second_num} = {first_num * second_num}")
prompt(f"{first_num} / {second_num} = {first_num / second_num}")
prompt(f"{first_num} // {second_num} = {float(first_num // second_num):.1f}")
prompt(f"{first_num} % {second_num} = {first_num % second_num}")
prompt(f"{first_num} ** {second_num} = {first_num ** second_num}")


# model answer:
def calculate(first, second, operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")

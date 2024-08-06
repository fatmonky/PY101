# 6 Aug 2024, my first try without reading the walk-through:

# Pseudocode:
# ask user for the first number, and assign this to variable 1
# ask user for the second number, and assign this to variable 2
# ask user for the tyupe of operation to perform: add, subtract, multiply or divide
# convert variables to int
# perform calculation, using match-case, and display the result.


# ask user for the first number, and assign this to variable 1
num1 = float(input("Enter the first number: "))
# ask user for the second number, and assign this to variable 2
num2 = float(input("Enter the second number: "))
# ask user for the tyupe of operation to perform: add, subtract, multiply or divide, and assign to variable operator
operator = input("What type of operation will you like to perform? Type\n'a' to add;\n's' to substract;\n'm' to multiply;\n'd' to divide.\n")

# perform calculation, using match-case, and display the result.
def calculation(num1, num2):
    match operator:
        case 'a':
            return int(num1 + num2)
        case 's':
            return int(num1 - num2)
        case 'm':
            return int(num1 * num2)
        case 'd':
            return (num1 / num2)

print(f"The result of your calculation is {calculation(num1,num2):.2f}.")

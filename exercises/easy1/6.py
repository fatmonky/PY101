"""
Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

Example 1
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.
Example 2
Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
"""

def sum_int(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

def prod_int(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total

# function test sum_int
#print(f"sum_int(5), expect 15, {sum_int(5)}")
# function test prod_int
#print(f"prod_int(6), expect 720, {prod_int(6)}")

user_number = int(input("Please enter an integer greater than 0: "))
user_choice = input(" Enter \"s\" to compute the sum, or \"p\" to compute the product. ")
match user_choice:
    case "s":
        print(f"The sum of the integers between 1 and {user_number} is {sum_int(user_number)}.")
    case "p":
        print(f"The prod of the integers between 1 and {user_number} is {prod_int(user_number)}.")
    case _:
        print("Invalid input: please try again!")

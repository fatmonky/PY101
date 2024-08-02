"""
Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?

"""
# my answer:
for num in range(1, 100):
    if num % 2 == 1:
        print(num) 

# bonus - answer:
# was stuck!

# model answer - uses increment of 2 in range. Very elegant!
for number in range(1, 100, 2):
    print(number)

#" consider adding a way for the user to specify the starting and ending values of the odd numbers.
start = int(input("Please input your starting number:"))
end = int(input("Please input your ending number:"))

for number in range(start, end + 1):
    if number % 2 == 1:
        print(number)

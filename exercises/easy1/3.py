# my answer, using the bonus approach:
for num in range(2, 100, 2):
    print(num)

# my answer, using the non-bonus approach:
for num in range(1, 99):
    if num % 2 == 0:
        print(num)

# my answer, allowing user to input starting and ending numbers:

start = int(input("Please input your starting number:"))
end = int(input("Please input your ending number:"))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)

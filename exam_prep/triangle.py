def triangle(num):
    for digit in range(1, num + 1):
        print(f"{(num - digit) * " "}{digit * "*"}")

triangle(3)
triangle(5)
triangle(9)

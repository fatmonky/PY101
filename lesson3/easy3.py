# try 1: 27 aug 24 312pm. To review: 2, 5.
#1
numbers = [1, 2, 3, 4]
#1.a.
numbers.clear()
print(numbers)
numbers = [1, 2, 3, 4]
#1.b.
while numbers:
    numbers.pop()
print(numbers)


# NOTE: to review
#2: It should throw an error, because + doesn't work as an operator for lists.
# model answer: [1, 2, 3, 4, 5] # in Python, + concatenates two lists.

#3:
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
# "hello there". str2 points to str1's value, and then is reassigned to "goodbye", but str1 still points to its original value.

#4:
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
# my_list1 = [{"first": 42}, {"second": "value2"}, 3, 4, 5]. Since my_list2 is a shallow copy, it references the original nested my_list1 elements. so changing my_list2's nested elements changes directly the values of nested elements in my_list1.

# NOTE: to review
#5:
#5a.
def is_color_valid(color):
    return color is "blue" or color is "green"
print(is_color_valid("blue"))
print(is_color_valid("green"))
print(is_color_valid("brown"))
print(is_color_valid("red"))

#5b.
def is_color_valid(color):
    return color == "blue" or color == "green"
print(is_color_valid("blue"))
print(is_color_valid("green"))
print(is_color_valid("brown"))
print(is_color_valid("red"))

# model answer:
def is_color_valid(color):
    return color in ["blue", "green"]
print(is_color_valid("blue"))
print(is_color_valid("green"))
print(is_color_valid("brown"))
print(is_color_valid("red"))


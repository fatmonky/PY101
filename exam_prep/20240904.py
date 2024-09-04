"""
# Strings
mashup = "thIs is How we type careLEssly"
cleaned = mashup.capitalize()
print(cleaned)

stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)
print(str1)
print(str2)
print(str3)

s1 = "Hello"
print(s1.isalpha())
s2 = "Hello World"
print(s2.isalpha())
s3 = "Hello!"
print(s3.isalpha())
s4 = "Hello123"
print(s4.isalpha())
s5 = ""
print(s5.isalpha())
s6 = "こんにち他"
print(s6.isalpha())
s7 = "HelloWorld"
print(s7.isalpha())
words = ["apple", "banana", "cherry"]
print(all(word.isalpha() for word in words))

string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()
result2 = string2.isalpha()
result3 = string3.isalpha()

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)

s1 = "123abc"
print(s1.isdigit())
s2 = "123$%^"
print(s2.isdigit())
s3 = ""
print(s3.isdigit())
s4 = "12345"
print(s4.isdigit())

print("Hello World".isalnum())
print("Hello@World".isalnum())
print("".isalnum())
print("Hello123".isalnum())


name = 'HELLO'

if name.isupper():
    print("WORLD")
else:
    print("world")

def punctuation_type(str):
    if str.upper():
        print('This is all caps')
    elif str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3)

str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!   How are you?   "
word_count = sum(1 for word in sentence.split() if word.isspace())
print(sentence.split())
print("Number of words in the sentence:", word_count)

s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))

s = "www.example.com"
print(s.lstrip('wcmo.'))

s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))

s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0"))

sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2)
print(words)

str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)

# Boolean vs Truthiness
truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print("Values:")
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

x = 5
y = 10
z = 15

print(x > 0 and y < 20)
print(not x == y)
print(x < y and y < z)
print(x > y or y > z)
print(not (x > y))

a = 10
b = 20

print(a < b < 30)
print(a > b or b == 20)

#4
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)

temperature = 25
time_of_day = "morning"

if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
    print("It's a pleasant day!")
else:
    print("It's either too hot or not the right time of day.")

num = 12

if num / 3 < 3 and num > 10:
    print("Hello") # False
elif num >= 8 and num < 6 or num > 4 and num < 16:
    print("Hello 2")
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")

print(range(0,10))
print(len(range(5, 15)))
print(range(1))
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))

example = range(0)
if example:
    print(list(example))
else:
    print(example)

def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if n <= 100:
            print(f'{number} is between 51 and 100')
        case _:
            print(f'{number} is greater than 100')
number_range(0)
number_range(25)

my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("Length of the list:", length_of_list)

lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_two)
else:
    print(lst_one)


my_list = [1, 2, 3, 4, 5]
ele = my_list.pop()
print("Popped element:", ele)
print("List after popping:", my_list)
ele1 = my_list.pop(1)
print("Popped element at index 1:", ele1)
print("Modified list after popping at index 1:", my_list)

elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)

ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dima(info):
    try:
        info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dima(ages))

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key)

my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)
for value in values:
    print(value)

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)
for key, value in items:
    print( key, value)

name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()  # Output: Hello, John!

def assign():
    var = 20
    print(var)

assign()

try:
    print(var)
except NameError as e:
    print("Error occurred")


var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)

var = 10

def function1():
    print(var)

function1()

def function2():
    var = 20
    print(var)

function2()
print(var)

def function1():
  x = 10

  def function2():
      y = 20
      print(x)

  function2()
  print(x)

function1()
print(x)
print(y)
"""

var = 10

def access():
    print(var)

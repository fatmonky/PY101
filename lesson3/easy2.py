# done 27 Aug 24: to review 3, 4, 5, 6, 8, 9

#1:
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
#1.a.
print(list(reversed(numbers)))
print(numbers) #showing numbers not mutated
#1.b.
print(numbers[4::-1]) #model answer: numbers[::-1]
print(numbers) #showing numbers not mutated

#2:
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
print(number1 in numbers)
print(number2 in numbers)

# NOTE: to revise
#3: 
def test_10_100(numb):
    if numb >= 10 and numb <= 100:
        return True
    return False
print(test_10_100(42))
print(test_10_100(100))
print(test_10_100(101))

# model answers:
"""
42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False
"""

# NOTE: to review
#4: 
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
numbers.pop(2) #model answer: del numbers[2]
print(numbers)

# NOTE: to review
#5:
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(type(numbers) is list)
print(type(table) is list)
#model answer:
"""
isinstance(numbers, list)  # True
isinstance(table, list)    # False
"""

# NOTE: to review
#6:
# I don't understand this question at all...
# model answer:
"""
title = "Flintstone Family Members"
centered_title = title.center(40)
"""

#7:
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(statement1.count('t'))
print(statement2.count('t'))

# NOTE: to review
#8:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print(ages.get("Spot", "doesn't exist"))
#model answer:
print("Spot" in ages)

#NOTE: to review
#9:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
new_ages = zip(ages, additional_ages)
print(dict(new_ages)) #WRONG.
#right answer: 
ages.update(additional_ages)
print(ages)

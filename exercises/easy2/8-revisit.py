"""
Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

ExamplesCopy Code
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
Bonus question: Try to solve the problem using list slicing.

def oddities(lst):
    new_lst = lst[::2]
    return new_lst

def oddities(lst):
    return lst[::2]
    """

def oddities(lst):
    new_list = []
    for idx in range(len(lst)):
        if idx % 2 == 0:
            new_list.append(lst[idx])

    return new_list


#answered with bonus!
print(oddities([2, 3, 4, 5, 6]))
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

# companion function which returns evens
def evens(lst):
    new_list = []
    for idx in range(len(lst)):
        if idx % 2 != 0 and idx != 0:
            new_list.append(lst[idx])
    return new_list

#tests
print(evens([1,2,3,4]))
print(evens([1]))

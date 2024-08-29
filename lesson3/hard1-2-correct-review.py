#try 1 27 Aug 24 558pm
#try 2 28 Aug 24 412pm
"""
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
"""
# answer: [1, 2]\n {'first':[1, 2]}. This is because dictionary is mutated by num_list.
# if we want to modify num_list but not dictionary, we can copy via .copy() or [:]

# answer try 2: The last line of the code outputs {'first':[1, 2]}. Python dictionaries and lists are mutable. line2 assigns the variable num_list to the value of dictionary['first'], which is a single element list [1]. line 3 mutates num_list, resulting in [1, 2]. since num_list points to dictionary['first'], the original dictionary's values are also mutated. i
# if we want to modify the code without changing the dictionary value, there are a few ways to do so. one way is to import copy, and do a deepcopy of the dictionary. 

import copy

dictionary = {'first': [1]}
new_dict = copy.deepcopy(dictionary)
num_list = new_dict['first']
num_list.append(2)

print(num_list)
print(dictionary)

# another way:

dictionary = {'first': [1]}
num_list = new_dict['first'].copy()
# or: num_list = new_dict['first'][:]
num_list.append(2)

print(num_list)
print(dictionary)

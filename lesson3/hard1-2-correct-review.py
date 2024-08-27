#try 1 27 Aug 24 558pm
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
# answer: [1, 2]\n {'first':[1, 2]}. This is because dictionary is mutated by num_list.
# if we want to modify num_list but not dictionary, we can copy via .copy() or [:]

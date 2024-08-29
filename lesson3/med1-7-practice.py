# try1 27 Aug 24 349pm
# try2 28 Aug 24 1028am
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)
print(munsters)
# answer: yes, because all the associated ages would be += 42, and the geners would be 'other'.

# try 2 answer: yes, the family's data gets ransacked.
# The Munsters' dictionary,munsters, consists of a key-value pair, with each value being a nested dictionary. In Python, dictionaries are mutable data-structures. When mess_with_demographics was called with munsters, a reference to munsters was directly passed as argument to mess_with_demographics. What was then mutated was the nested dictionaries, which were accessed and modified. 
# Thus, mess_with_demographics directly mutated munsters, not just a copy of munsters. If Spot wanted to play around with a copy, he would need to import copy, and use copy.deepcopy() to create a copy of munsters, and call mess_with_demographics with the copy as argument. 

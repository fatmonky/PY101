"""
Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

Example
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
"""

def greetings(lst, dic):
    full_name = lst[0] + " " + lst[1] + " " + lst[2]
    return f"Hello {full_name}! Nice to have a {dic["title"]} {dic["occupation"]} around."
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)

# model answer:
"""

def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
           f"{status['title']} {status['occupation']}"
           "around.")
Discussion
We use the join method to change the list into a full name with appropriate spacing. For the dictionary, we access the items by their keys.

Finally, we use f-string formatting to combine everything into a single string, resulting in a concise and readable way to format the final output.

Note that the parentheses on the return are necessary here. Without them, Python won't deal with the continuation lines correctly.

"""

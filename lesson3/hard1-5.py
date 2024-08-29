#try1 27 Aug 24 619pm
#try2 28 Aug 24 429pm
"""
What do you expect to happen when the greeting variable is referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)
"""
if False:
    greeting = "hello world"

print(greeting)

# answer: get a NameError, as greeting is not defined.
# answer try 2: in this code, greeting is a local variable which is assigned the string "hello world" only if False is true. However, since the if statement is not executed, greeting is not assigned. print(greeting) will then throw a NameError, for using an undefined variable. 

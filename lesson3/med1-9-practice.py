# try 1 27 Aug 24 358pm
# try 2 27 Aug 24 1045am

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo())

# answer: False, because foo() returns yes, which means bar's return is False

# answer: False. foo() evaluates to return "yes", which is passed into bar as argument. 
# since bar's argument is "yes", (param == "no") evaluates to False; due to short-circuit evaluation, the right-hand-side of the and-expression is not executed, and bar returns False. 

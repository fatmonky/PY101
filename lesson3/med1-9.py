# try 1 27 Aug 24 358pm

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo())

# answer: False, because foo() returns yes, which means bar's return is False

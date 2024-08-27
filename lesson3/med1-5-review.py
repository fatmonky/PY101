# try1 27 Aug 24 342pm
nan_value = float("nan")

print(nan_value == float("nan"))
# answer: ValueError.
# bonus question "how to reliably test if a value is nan?"
# answer: dunno! 

#model answer:
# False, because nan is not a number, and cannot be compared using == in Python. 
# to test nan, use math.isnan(<value to test>)

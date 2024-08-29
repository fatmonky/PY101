# try1 27 aug 24 401pm
# try2 28 Aug 24 1048am
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
# answer: id for a and b are the same, but not c, which points to a. So answer is False. 
# model answer: The output is True.

#Here, a and c reference the same object in memory, so their ids are the same. b will, in this case, have the same id as a and c due to interning. Therefore, the code will output True.

#In Python, there's a predefined range of integers, specifically from -5 to 256, for which memory locations are pre-assigned. When you reference an integer within this span, Python consistently points to the same memory spot. This strategy enhances efficiency since these particular numbers are commonly utilized in many programming scenarios.

#However, when you work with integers outside of this specific range, Python doesn't assure that it will consistently point to the same memory address for identical values across different variables.

# practice answer 2: the code will print True. a and b reference the same integer object value, 42, due to interning. c is assigned to a, so it also points to the value 42. However, to note, that this integer interning doesn't work outside of integer values -5 to 256: Python will not consistently point to the same memory address for identical values across different variables. 

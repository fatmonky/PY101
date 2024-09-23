print(1 or 2 and 3)
print(0 or 2 and 3)
print(1 or 0 and 3)
print(1 or 2 and 0)
print(0 or 0 and 3)
print(0 or 2 and 0)
print(1 or 0 and 0)
print(0 or 0 and 0)
print("\n")
print(1 and 2 or 3)
print(0 and 2 or 3)
print(1 and 0 or 3)
print(1 and 2 or 0)
print(0 and 0 or 3)
print(0 and 2 or 0)
print(1 and 0 or 0)
print(0 and 0 or 0)

"""
My first try answer:
1
True
1
1
False
False
1
False

True
False
False
True
False
False
False
False

Run and see the real results! 
# lessons learnt: truthy != True, falsy != False.
"""

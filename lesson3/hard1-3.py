# try 1 27 Aug 24 602pm

#A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
# answer: one is ["one"], two is ["two"], three is ["three"]. mess_with_vars has no return value, so doesn't change or reassign one, two or three at the global level. 
# model answer:

#B:
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
# answer: one is ["one"], two is ["two"], three is ["three"]. mess_with_vars has no return value, so doesn't change or reassign one, two or three at the global level. 
#model answer:

#C:
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
#answer: one is two, two is three, three is one. This is different, because mess_with_vars is mutating the lists (function arguments), so the global variables will return different list elements. 
#model answer: In this case, the mess_with_vars function modifies the content of the lists directly. Since lists in Python are mutable and passed by reference, the changes are reflected outside the function.
# model answer: also includes observation of variable shadowing in all three functions.

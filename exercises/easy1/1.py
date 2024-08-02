#Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def isodd(num):
    if abs(num) % 2 == 0:
        return False
    else:
        return True

#test
print(f"isodd(0), expect False, returns {isodd(0)}")
print(f"isodd(1), expect True, returns {isodd(1)}")
print(f"isodd(2), expect False, returns {isodd(2)}")
print(f"isodd(-1), expect True, returns {isodd(-1)}")
print(f"isodd(-2), expect False, returns {isodd(-2)}")

#model answer:
"""
def is_odd(number):
    return abs(number) % 2 == 1
# very elegant solution! checks for odd, vs my solution which checks for even.
"""

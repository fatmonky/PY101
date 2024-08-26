# Exercises at end of Variable Scope chapter:
# 1
# my answer: '5', because num is a global variable called & printed by my_func.

# Ex2: my answer - 5, because my_func's num is local to my_func, and is not the same as global num. so line 7 prints global num, and not num in my_func's scope.

# 3:  10, because my_func re-assigns num globally from 5 to 10, and my_func is called. 

#(revisit) 4: NameError, because while outer_var is outside of inner(), outer() is only called after inner(), so outer_var isn't assigned when inner() is called. 
# model answer: prints "Hello world". 
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# 5: NameError, because num is local to my_func's scope, and is undefined outside of my_func. i

# 6: It will print "Inner1: 25", "Inner2: 15" twice. 
# model answer: not twice, just once, which is my mistake in thinking inner_func1 and inner_func2 get called twice.
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

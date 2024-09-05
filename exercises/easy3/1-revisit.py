"""def repeat(string, times):
    print((string + "\n") * times) 
"""
# model answer:
def repeat(string, times):
    for _ in range(times):
        print(string)

repeat("Hello", 3)
repeat("Hello World", 3)

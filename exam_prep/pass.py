a = "a"
b = "b"

def joiner(string1, string2):
    string1 += string1
    string2 += string2

joiner(a, b)

print(a)  # a
print(b)  # b

a = ["a"]
b = ["b"]

def joiner2(string1, string2):
    string1 += string1
    string2 += string2

joiner2(a, b)

print(a)  # a
print(b)  # b



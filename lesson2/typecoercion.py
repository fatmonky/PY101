non_numeric_str = ["abc"]
try:
    non_numeric_integer = int(non_numeric_str)
except ValueError:
    print("cannot convert to int")
except TypeError:
    print("wrong type for conversion")
else:
    print(f"the new int is {non_numeric_integer}")

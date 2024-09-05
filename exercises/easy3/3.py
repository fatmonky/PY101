def print_in_box(string):
    # calculate string length
    string_length = len(string)
    # first, print empty box
    print("+-" + (string_length * "-") + "-+")
    print("| " + (string_length * " ") + " |")
    print("| " + string + " |")
    print("| " + (string_length * " ") + " |")
    print("+-" + (string_length * "-") + "-+")

print_in_box("")
print_in_box("To boldly go where no one has gone before.")

# model answer: creates three separate variables for edge, empty line and filled lines. These are then

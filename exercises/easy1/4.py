"""
Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
"""

# my answer
SQ_M_TO_SQ_FT = 10.7639

room_length_m = float(input("Please enter the length of the room, in meters: "))
room_width_m = float(input("Please enter the width of the room, in meters: "))

def room_area_m(length, width):
    return length * width

print(f"The room area in square meters is: {room_area_m(room_length_m, room_width_m)}")
print(f"The room area in square feet is: {room_area_m(room_length_m, room_width_m) * SQ_M_TO_SQ_FT}")

# model answer
# model answer includes format specification {:.2f} to format to two decimal places. Also uses variables instead of function.

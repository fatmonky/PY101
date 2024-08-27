# try1 27 Aug 346pm

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# answer: 34. answer was not reassigned by mess_with_it, so it is still 42.the printed value is 42 - 8 = 34. 
# new_answer's value is pointing to 42 + 8, due to mess_with_it(answer)

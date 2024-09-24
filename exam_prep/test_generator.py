import random
import os

"""
Command-Line Program to randomly generate practice questions from
Launch School's PY101 curriculum questions.

How to use:

1. Run the program in the command line: python test_generator.py
This should output five practice questions like the following:
	Practice question 1: answer Exercises / Easy1 / 3
	Practice question 2: answer Lesson3 / Easy2 / 8
	Practice question 3: answer Exercises / Easy 3 / 4
	Practice question 4: answer Lesson3 / Medium / 4
	Practice question 5: answer Lesson3 / Hard / 4

2. Look up the respective questions in LaunchSchool's curriculum, 
    either in PY101 Lesson3 or in Exercises. 

3. Practice answering those questions whenever you want. 

"""

problem_bank = {
        "Exercises": {
            "Easy1": 11,
            "Easy2": 12,
            "Easy3": 10,
            },
        "Lesson3": {
            "Easy1": 10,
            "Easy2": 9,
            "Easy3": 5,
            "Medium": 10,
            "Hard":  5,
            },
        }
enum_keys = list(problem_bank.keys())
enum_subcat = list(problem_bank["Exercises"].keys())

def select_easy_category():
    return random.choice(enum_keys)

def select_easy_subcat():
    return random.choice(enum_subcat)

def clear_screen():
    os.system("clear")

def generate_easy_qn():
    for num in range(1, 4):
        print_output = (
        f"Practice question {num}: answer {select_easy_category()}\
 / {select_easy_subcat()} / question \
{random.randint(1, \
problem_bank[select_easy_category()][select_easy_subcat()])}")
        print(print_output)

def main():
    while True:
        clear_screen()
        generate_easy_qn()
        print(f"Practice question 4: answer Lesson3 / Medium / question \
{random.randint(1, problem_bank["Lesson3"]["Medium"])}")
        print(f"Practice question 5: answer Lesson3 / Hard / question \
{random.randint(1, problem_bank["Lesson3"]["Hard"])}")
        again = input("\n=> Would you like to generate another set of 5\
questions? Y/n\n")
        if again in ['N', 'n']:
            break
    print("Good luck on your PY109 exam and interview!")

main()

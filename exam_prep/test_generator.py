import random

"""
Command-Line Program to randomly generate practice questions from
Launch School's PY101 curriculum questions.
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

random_easy_category = select_easy_category()
random_easy_category2 = select_easy_category()
random_easy_category3 = select_easy_category()
random_easy_subcat = select_easy_subcat()
random_easy_subcat2 = select_easy_subcat()
random_easy_subcat3 = select_easy_subcat()


print(f"Practice question 1: answer {random_easy_category} / {random_easy_subcat} / question {random.randint(1, problem_bank[random_easy_category][random_easy_subcat])}")
print(f"Practice question 2: answer {random_easy_category2} / {random_easy_subcat2} / question {random.randint(1, problem_bank[random_easy_category2][random_easy_subcat2])}")
print(f"Practice question 3: answer {random_easy_category3} / {random_easy_subcat3} / question {random.randint(1, problem_bank[random_easy_category3][random_easy_subcat3])}")
print(f"Practice question 4: answer Lesson3 / Medium / question {random.randint(1, problem_bank["Lesson3"]["Medium"])}")
print(f"Practice question 5: answer Lesson3 / Hard / question {random.randint(1, problem_bank["Lesson3"]["Hard"])}")
#print(f"Practice question 5: answer {problem_bank["Lesson3"]} / {random.randint(problem_bank["Lesson3"]["Hard"])}")

# desired output
# Practice question 1: answer Exercises / Easy1 / 3
# Practice question 2: answer Lesson3 / Easy2 / 8
# Practice question 3: answer Exercises / Easy 3 / 4
# Practice question 4: answer Lesson3 / Medium / 4
# Practice question 5: answer Lesson3 / Hard / 4

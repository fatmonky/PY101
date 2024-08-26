"""
Command Line rock-paper-scissors game
"""
#TODO: pseudocode of logic (done)
#TODO: write out code (done)
#TODO: test code through play. (done)
#TODO: pylint code

import os
import json
import random

with open('rps_messages.json','r') as file:
    MSG_DATA = json.load(file)

def clear_screen():
    os.system("clear")

def prompt(message):
    print(f"==>{message}")

def get_user_choice():
    prompt(MSG_DATA["user_instruction"])
    choice = input().lower()
    while choice not in MSG_DATA["valid_choices"].keys():
        prompt(MSG_DATA["invalid_choice"])
        prompt(MSG_DATA["user_instruction"])
        choice = input().lower().strip()
    return choice

def display_computer_choice(choice):
    prompt(f"The computer chose: {choice.title()}")

def display_user_choice(choice):
    prompt(f"You chose: {choice.title()}")

def determine_winner(user, computer, user_score, computer_score):
    # if user has rock and computer has scissors
    # if user has paper and computer has rock
    # if user has scissors and computer has paper
    # user won
    if ((user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")):
        prompt("You have won!")
        return True

    #elif user has rock and computer has paper
    #elif user has paper and computer has scissors
    #elif user has scissors and computer has rock
    # computer won
    elif ((user == "rock" and computer == "paper") or
    (user == "paper" and computer == "scissors") or
    (user == "scissors" and computer == "rock")):
        prompt("The Computer Won!")
        return False

    # else
    # it's a tie
    else:
        prompt("It's a Tie!")
        return None


def get_play_again():
    while True:
        prompt("Play again? Y/n")
        play_again = input().lower()
        if play_again not in ["Y", "y", "n", "N"]:
            prompt("That's not a valid response.")
            prompt("Play again? Y/n")
            play_again = input().lower().strip()
        if play_again in ["Y","y","n","N"]:
            break
    return play_again

def main():
    clear_screen()
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        user_choice_value = MSG_DATA[
                "valid_choices"].get(user_choice, "invalid option")
        #select random computer choice
        computer_choice_value = random.choice(
                list(MSG_DATA["valid_choices"].values()))
        display_computer_choice(computer_choice_value)
        display_user_choice(user_choice_value)

        # compare user_choice with computer_choice, display winner
        user_win = determine_winner(user_choice_value, computer_choice_value,
                         user_score, computer_score)
        if user_win:
            user_score += 1
        elif user_win is False:
            computer_score += 1

        # option to play again
        if get_play_again() in ["N","n"]:
            break

    clear_screen()
    # end and display farewell and score
    prompt(f"Your final score is {user_score} vs. the computer score of {computer_score}")
    prompt("Goodbye!")

main()

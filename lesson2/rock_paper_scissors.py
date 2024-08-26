"""
Command Line rock-paper-scissors game
"""
# TODO: best of five (done)
# TODO: add lizard and spock into winning logic
# TODO: shortened input for spock (done)
# TODO: fix Pylint complaints

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
    choice = input().lower().strip()
    while choice not in MSG_DATA["valid_choices"].keys():
        prompt(MSG_DATA["invalid_choice"])
        prompt(MSG_DATA["user_instruction"])
        choice = input().lower().strip()
    return choice

def display_computer_choice(choice):
    prompt(f"The computer chose: {choice.title()}")

def display_user_choice(choice):
    prompt(f"You chose: {choice.title()}")

def determine_winner(user, computer):
    if ((user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")):
        prompt("You have won!")
        return True
    if ((user == "rock" and computer == "paper") or
    (user == "paper" and computer == "scissors") or
    (user == "scissors" and computer == "rock")):
        prompt("The Computer Won!")
        return False
    prompt("It's a Tie!")
    return None

def change_winner_scores(who_wins, score1, score2):
    if who_wins:
        score1 += 1
    elif who_wins is False:
        score2 += 1
    return score1, score2

def get_play_again():
    while True:
        prompt(MSG_DATA["play_again"])
        play_again = input().lower().strip()
        if play_again not in ["Y", "y", "n", "N"]:
            prompt(MSG_DATA["invalid_choice"])
            prompt(MSG_DATA["play_again"])
            play_again = input().lower().strip()
        if play_again in ["Y","y","n","N"]:
            break
    return play_again

def display_current_score(user_score,computer_score):
    print("\n")
    prompt(f"Your current score: {user_score}")
    prompt(f"vs. the computer score: {computer_score}")

def display_scores_farewell(user_score,computer_score):
    prompt(f"Your final score is {user_score}")
    prompt(f"vs. the computer score of {computer_score}")
    prompt("Goodbye!")

def best_of_five(user_score, computer_score):
    if user_score >= 3:
        prompt("Congratulations! You've won!")
        return False
    if computer_score >= 3:
        prompt("Sorry to say, you lost... Better luck next time?")
        return False
    return True


def main():
    clear_screen()
    user_score = 0
    computer_score = 0
    tournament_on = True
    while tournament_on:
        clear_screen()
        user_choice = get_user_choice()
        user_choice_value = MSG_DATA[
                "valid_choices"].get(user_choice, "invalid option")
        computer_choice_value = random.choice(
                list(MSG_DATA["valid_choices"].values()))
        display_computer_choice(computer_choice_value)
        display_user_choice(user_choice_value)

        user_win = determine_winner(user_choice_value, computer_choice_value)
        user_score, computer_score = change_winner_scores(user_win, user_score, computer_score)
        display_current_score(user_score, computer_score)
        
        tournament_on = best_of_five(user_score, computer_score)
        if (tournament_on is False) or (get_play_again() in ["N","n"]):
            break

    display_scores_farewell(user_score, computer_score)

main()

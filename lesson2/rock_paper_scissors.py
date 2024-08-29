"""
Command Line rock-paper-scissors game
"""

import os
import json
import random

MAX_SCORE = 3

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
    prompt(f"You chose: {choice.title()}\n")

def player_wins(player_choice, computer_choice):
    return computer_choice in MSG_DATA["WINNING_CHOICES"][player_choice]

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
        if play_again not in MSG_DATA["play_again_choices"]:
            prompt(MSG_DATA["invalid_choice"])
            prompt(MSG_DATA["play_again"])
            play_again = input().lower().strip()
        if play_again in MSG_DATA["play_again_choices"]:
            break
    return play_again

def display_current_score(user_score,computer_score):
    prompt(f"Your current score: {user_score}")
    prompt(f"vs. the computer score: {computer_score}\n")

def display_scores_farewell(user_score,computer_score):
    prompt(f"Your final score is {user_score}")
    prompt(f"vs. the computer score of {computer_score}\n")
    prompt("Goodbye!")

def best_of_five(user_score, computer_score):
    if user_score >= MAX_SCORE:
        return False
    if computer_score >= MAX_SCORE:
        return False
    return True

def player_wins_tournament(user_score):
    return user_score >= MAX_SCORE

def display_winner(user_score):
    if player_wins_tournament(user_score):
        prompt(MSG_DATA["congratulations"])
    else:
        prompt(MSG_DATA["sorry"])

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

        user_win = player_wins(user_choice_value, computer_choice_value)
        user_score, computer_score = change_winner_scores(user_win,
                                                          user_score,
                                                          computer_score)
        display_current_score(user_score, computer_score)

        tournament_on = best_of_five(user_score, computer_score)
        if not tournament_on:
            display_winner(user_score)
            break
        if get_play_again() in MSG_DATA["not_playing_again"]:
            break
    if tournament_on is True:
        display_scores_farewell(user_score, computer_score)

main()

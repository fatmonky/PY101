"""
Command Line rock-paper-scissors game
"""
#TODO: pseudocode of logic
#TODO: write out code
#TODO: test code through play.
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
        choice = input().lower()
    return choice

def display_computer_choice(choice):
    prompt(f"The computer chose: {choice.title()}")

def display_user_choice(choice):
    prompt(f"You chose: {choice.title()}")

def determine_winner(user, computer):
    # if user has rock and computer has scissors
    # if user has paper and computer has rock
    # if user has scissors and computer has paper
    # user won
    if ((user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")):
        prompt("You have won!")

    #elif user has rock and computer has paper
    #elif user has paper and computer has scissors
    #elif user has scissors and computer has rock
    # computer won
    elif ((user == "rock" and computer == "paper") or
    (user == "paper" and computer == "scissors") or
    (user == "scissors" and computer == "rock")):
        prompt("The Computer Won!")

    # else
    # it's a tie
    else:
        prompt("It's a Tie!")

def main():
    clear_screen()
    user_choice = get_user_choice()
    user_choice_value = MSG_DATA[
            "valid_choices"].get(user_choice, "invalid option")
    #select random computer choice
    computer_choice_value = random.choice(
            list(MSG_DATA["valid_choices"].values()))
    display_computer_choice(computer_choice_value)
    display_user_choice(user_choice_value)

    # compare user_choice with computer_choice, display winner
    determine_winner(user_choice_value, computer_choice_value)
    

    # option to play again
    
main()

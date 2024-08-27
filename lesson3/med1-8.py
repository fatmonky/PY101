# try1 27 Aug 24 353pm
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# answer working: rps(rps("paper", "rock"), "rock")
# working:=> rps("paper", "rock")
# answer: => "paper"

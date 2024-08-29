# try1 27 Aug 24 353pm
# try2 28 Aug 24 1037am

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

# The first call of rps yields "paper", "rock" respectively. 
# rps is then called with "paper", "rock" as arguments: this yields "paper.
# rps is then called for one final time, with "paper" and "rock" as arguments: this yields the final result of "paper".

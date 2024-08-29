# try 1
def main():
    name = input("What is your name? ")
    if "!" in name: #model answer: use if name.endswith("!"):
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}.")

main()

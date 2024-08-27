# try 1: 27 Aug 24 318pm 
# NOTE: to review

# assign variable to string
flintstones = "The Flintstones Rock!"

# for each iteration until 10,
# prepend '-' to flintstones
# re-assigne prepended flintstones to flintstones
# add +1 to index
index = 0
while index < 10:
    flintstones = "-" + flintstones
    print(flintstones)
    index += 1

# model answer:
for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')

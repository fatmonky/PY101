# attempt 1 27 Aug 24 225pm - revise qn 9.
#1: yes, because the index is out of bounds. 

#2:
def ends_with_exclamation(string):
    if string.endswith("!"):
        return True
    return False
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
print(ends_with_exclamation(str1))
print(ends_with_exclamation(str2))

#3: 
famous_words = "seven years ago..."
#3.a.
print("Four score and " + famous_words)
#3.b.
print(f"Four score and {famous_words}")

#4: 
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
print(munsters_description.capitalize())

#5: 
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

#6: 
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print("Dino" in str1)
print("Dino" in str2)

#7: 
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)

#8:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])
print(flintstones)

# NOTE: to revise
#9:
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
print(advice[:38])
print(advice.split("house")[0]) #model answer: very elegant!

#10:
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important","urgent"))


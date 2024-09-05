def get_something(something):
    if something[0] in ['a', 'A']:
        print(f"Enter an {something}: ")
    else:
        print(f"Enter a {something}: ")
    something = input()
    return something

def get_noun():
    noun = get_something("noun")
    return noun

def get_verb():
    verb = get_something("verb")
    return verb

def get_adjective():
    adjective = get_something("adjective")
    return adjective

def get_adverb():
    adverb = get_something("adverb")
    return adverb

def generate_story(verb, noun, adjective, adverb):
    print(f"How might we {verb} your {adjective} {noun} in a {adverb} way?")
    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
    print(f"The {adjective} {noun} {verb}s {adverb} over the lazy dog.")
    print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")


def main():
    noun = get_noun()
    verb = get_verb()
    adjective = get_adjective()
    adverb = get_adverb()
    generate_story(verb, noun, adjective, adverb)

main()

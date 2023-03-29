# basic translator - draft translator
# take in string and translate to different language

# Giraffe Language
# all vowels -> g
# dog -> dgg
# cat -> cgt

def tranlate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": # letter.lower() in "aeiou"
            if letter.isupper():
                translation = translation + "G"
            else: translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(tranlate(input("Enter a phrase: ")))
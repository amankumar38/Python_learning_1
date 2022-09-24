def translator(phrase):
    translation = ""
    for words in phrase:
        if words in "AEIOUaeiou":
            if words.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + words
    return translation


print(translator(input("Enter the phrase: \n")))

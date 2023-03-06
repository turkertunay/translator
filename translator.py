def translator(word):

    translated_word = ""
    for letter in word:
        if letter == "p":
            translated_word = translated_word + "b"
        elif letter == "t":
            translated_word = translated_word + "d"
        elif letter == "k":
            translated_word = translated_word + "g"
        else:
            translated_word = translated_word + letter



    return translated_word

print(translator(input("Enter the word you want to translate: ")))



sentence_to_capitalize = input("Let's capitalize all first letters! Give me a sentence! ")
next_letter_capped = False
first_loop = True

for letter in sentence_to_capitalize:
    if first_loop == True:
        letter = letter.upper()
        first_loop = False
    elif next_letter_capped == True:
        letter = letter.upper()
        next_letter_capped = False
    elif letter == " ":
        next_letter_capped = True
    print(letter)
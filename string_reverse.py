word_to_be_reversed = input("Give me a word to reverse! ")
reversed_word = ""
list_to_be_reversed = []
reversed_word_list = []
length_of_word = len(word_to_be_reversed) -1

for letter in word_to_be_reversed:
    list_to_be_reversed.append(letter)

while length_of_word>=0:
    reversed_word += list_to_be_reversed[length_of_word]
    length_of_word -= 1
print(f"Your reversed word is {reversed_word}.")


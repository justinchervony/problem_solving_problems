string_to_compress = input("Give me a one-word string to compress! ")
number_of_letter = 1
previous_letter = ""
first_loop = True
loop_count = 1
string_length = len(string_to_compress)
compressed_string = ""

for letter in string_to_compress:
    if first_loop == True:
        first_loop = False
    #elif loop_count == string_length:
    elif letter == previous_letter:
        number_of_letter += 1
        if loop_count == string_length:
            compressed_string += f"{number_of_letter}{letter}"
    elif letter != previous_letter:
        if number_of_letter == 1:
            compressed_string += previous_letter
            if loop_count == string_length:
                compressed_string += letter
        else:
            compressed_string += f"{number_of_letter}{previous_letter}"
            number_of_letter = 1
            if loop_count == string_length:
                compressed_string += letter
    previous_letter = letter
    loop_count += 1
print(compressed_string)
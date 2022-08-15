"""
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
Test your program with the data we've provided for you.
""" 


# creat user input variable and make string upper case:
user_word = input().upper()

# loop through string:
for letter in user_word:
    # check for letter 'A':
    if letter == 'A':
        # continue
        continue
    # check for letter 'E':
    elif letter == 'E':
        # continue
        continue
    # check for letter 'I':
    elif letter == 'I':
        # continue:
        continue
    # check for letter 'O':
    elif letter == 'O':
        # continue:
        continue
    # check for letter 'U':
    elif letter == 'U':
        # continue
        continue
    # else print remaining string: one letter per line
    else:
        # print statement:
        print(letter, end = '\n')
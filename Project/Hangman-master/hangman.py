"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~  HANGMAN  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

""" 
This is a version of Hangman coded in Python!

There are 5 different sections that complete/contain the following:

1) setting initial variables, including the difficulty, and importing
   the Brown University Corpus
2) all the functions that will be used in making the initial board, the
   print_board function, and a call to the make_initial_board fuction
3) creating a sequence to construct the man as the player makes incorrect 
   guesses
4) a take_input function that essentially collects and processes all 
   input needed from the player, and a word_match function
5) the actual game loop

"""




"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~SECTION 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~Setting Initial Variables~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# This will import the 'random' module that will be used in selecting a word.
from random import choice



# The next few lines will set two variable called 'max_length' and 'min_length'
# that will set the maximum length of the word that needs to be guessed, which 
# will be chosen soon. Essentially, these lines set the difficulty of the game.
#
# IMPORTANT NOTE: The code here only attempts to create a way to find out how
# difficult it is to guess a word based on the length of the word. Due to the
# randomness of choosing the word, the actual difficulty may not always reflect
# the difficulty the player chooses, but the method used here will often work
# to accurately pick a word that reflects the difficulty the player chooses. 
# This is not the only way to find the difficulty of a word, and other ways can
# be implemented, based on how many vowels are in the word or how many different
# letters there are, for example. This section is especially open to alteration
# for other approaches! Additionally, the code in this section can be commented
# out, and user-chosen values for max_length and min_length can be used.

difficulty = raw_input("Set the difficulty to either easy, medium, or hard:")

difficulty = difficulty.lower()

while difficulty != "hard" and difficulty != "medium" and difficulty != "easy":
	difficulty = raw_input("Please enter 'easy', 'medium', or 'hard':")
	difficulty = difficulty.lower()

if difficulty == "easy":
	min_length = 6
	max_length = 7
elif difficulty == "medium": 
	min_length = 8
	max_length = 10
else:
	min_length = 5
	max_length = 5



# The next few lines will randomly select the initial word from the Brown 
# University Corpus. If you don't have access to it, you could comment out
# the next two lines, and uncomment the word list that follows. You could 
# also add words to this word list. 

from nltk.corpus import brown

word_list = brown.words()

"""
word_list = ["concentrate", "deviate", "house", "school", "answer", "wheel", "court", "mother", "food", "computer", "color", "sweater"]
"""

answer = choice(word_list)
answer_length = len(answer)
while answer_length < min_length or answer_length > max_length or (not answer.isalpha()):
    answer = choice(word_list)
    answer_length = len(answer)
	

answer = answer.lower()



# This is a list of all the letters that have been guessed, including the
# phrase "Used Letters: " at the zero index for display purposes.
used = ["Used Letters: "]



# The 'attempt' variable holds the current progress of the player in guessing
# the word by forming a list of strings made up of the correctly guessed 
# letters, and a "__ " for each unknown letter, as well as "Word: " at the 
# zero index for display purposes.
attempt = ["Word: "]
attempt.extend(["__ "] * len(answer))



# The 'guess' variable will be used to keep track of how many guesses the
# player has made.
guess = 0



# The 'max_guesses' variable is used to set the maximum number of guesses
# the player can make. Note that if you change this from the value 8, 
# the board's display of the hanging man will be off, but the game will
# progress normally until max_guesses is zero.
max_guesses = 8



# The game board is represented as a list of lists of strings. Here, it
# is set as an empty list, but the 'make_initial_board' procedure will 
# setup the initial board by appending onto this initial empty list.
board = []





"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~SECTION 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~Creating and Displaying the Board~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


"""
The following functions all behave similarly: make_row2, make_row3,
make_row4to8, make_row9, and make_border. Each one displays the
corresponding row of the board for the player. Each of these functions
takes in a list of list of strings, alol, that represents a board,
and outputs a new board with the appropriate row appended onto alol.
Note that 'make_border' creates rows one and ten.
""" 
def make_row2(alol):
    row = ["|"]
    row.extend([" "] * 4)
    row.extend(["_"] * 8)
    row.extend([" "] * 6)
    row.extend(["|"])
    alol.append(row)
    return alol

def make_row3(alol):
    row = ["|"]
    row.extend([" "] * 4)
    row.extend(["|"])
    row.extend([" "] * 6)
    row.extend(["|"])
    row.extend([" "] * 6)
    row.extend(["|"])
    alol.append(row)
    return alol

def make_rows4to8(alol):
    row = ["|"]
    row.extend([" "] * 4)
    row.extend(["|"])
    row.extend([" "] * 13)
    row.extend(["|"])
    alol.append(row)
    return alol

def make_row9(alol):
    row = ["|"]
    row.extend([" "])
    row.extend(["^"] * 7)
    row.extend([" "] * 10)
    row.extend(["|"])
    alol.append(row)
    return alol

def make_border(alol):
    alol.append(["-"] * 20)
    return alol



# Input: a list of list of strings, alol, that represents a board
# Ouput: a new board with the guessing progress stored
# as a list of strings in a new row of the board
def display_word(alol):
    return alol.append(attempt)



# Input: a list of list of strings, alol, that represents a board
# Output: a new board with all of the previously guessed letters 
# stored as a list of strings in a new row of the board    
def display_used_letters(alol):
    return alol.append(used)
    


# Input: a list of list of strings, alol, that represents a board,
# and normally, alol is an empty list
# Output: the initial board that is used in playing hangman
def make_initial_board(alol):
    make_border(alol)
    make_row2(alol)
    make_row3(alol)
    for x in range(1,6):
        make_rows4to8(alol)
    make_row9(alol)
    make_border(alol)
    alol.append([] * 20)
    display_word(alol)
    alol.append([] * 20)
    display_used_letters(alol)
    return alol
    

# This call creates the initial board from the inital value of board,
# which was an empty list.
make_initial_board(board)



# Input: a list of list of strings, alol, that represents a board
# Output: a display of the current board, including a line
# that indicates how many guesses a player has left    
def print_board(alol):
    guesses_left = max_guesses - guess
    for row in alol:
        print "".join(row)
    print "Guesses left: " + str(guesses_left)





"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~SECTION 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~Functions to Create the Hanging Man~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


"""
The following functions all behave similarly: add_head, add_body,
add_left_leg, add_right_leg, add_left_arm, add_right_arm, add_left_foot,
add_right_foot. Each function has no input, but each one alters the
playing board in a certain way indicated by the function name. Together,
these functions can display the hanging man on the board.
"""
def add_head():
    board[3][12] = "O"
    return board

def add_body():
    board[4][12] = "|"
    board[5][12] = "|"
    return board
    
def add_left_leg():
    board[6][11] = "/"
    return board
    
def add_right_leg():
    board[6][13] = "\\"
    return board
    
def add_left_arm():
    board[4][11] = "\\"
    return board

def add_right_arm():
    board[4][13] = "/"
    return board

def add_left_foot():
    board[6][10] = "_"
    return board

def add_right_foot():
    board[6][14] = "_"
    return board


# Input: none
# Output: an altered version of the current playing board
# in which, based on the number of incorrect guesses the
# player has made, a different part of the hanging man
# is displayed
# Note: if max_guesses is different from its original value
# of 8, the hanging man will not display properly as the
# game progresses

def add_sequence():
    if guess == 7:
        add_right_arm()
    elif guess == 6:
        add_left_arm()
    elif guess == 5:
        add_right_foot()
    elif guess == 4:
        add_left_foot()
    elif guess == 3:
        add_right_leg()
    elif guess == 2:
        add_left_leg()
    elif guess == 1:
        add_body()
    else:
        add_head()
    return board





"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~SECTION 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~take_input and word_match Functions~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""      


"""
'take_input' is a function that takes in no parameters, but asks the user
for input multiple times, and processes through all of the essential user 
input that is involved in hangman.

First, the 'attempt' and 'guess' variables are made global so that they
can be accessed and changed later on.

The first task that 'take_input' accomplishes involves asking the user whether
they want to enter a letter or guess the word. The user is prompted to do this
until he or she enters a string that, when in all lowercase, is either 'letter'
or 'word'.

If the user wants to guess a letter, 'take_input' ensures that the letter is only
a single character and has not been guessed before. If either of these conditions
is false, the user is prompted to enter a letter again.

If the letter is in the word (represented as the variable 'answer'), 'attempt' is 
changed accordingly so that corresponding blanks are removed. If the letter is not 
in the word, 'add_sequence' is called to add on the next part of the hanging man, 
and 'guess' is incremented by one. In either case, though, the guessed letter is 
stored in the 'used' variable, which is a list.

If the user wants to guess the word, 'take_input' first makes the string all lowercase,
then checks to see if it is the same as the 'answer' variable. If so, the game is over,
the 'attempt' variable is changed accordingly so that it no longer contains blanks,
and the game loop takes care of the rest. If the guess is incorrect, 'add_sequence' is
called and 'guess' is incremented by one.
"""

def take_input():
    global attempt
    global guess
    
    input_type = raw_input("Type if you want to guess a letter or word:")
    input_type = input_type.lower()
    
    while input_type != "letter" and input_type != "word":
        input_type = raw_input("You can only guess a 'letter' or a 'word':")
        input_type = input_type.lower()

    else:
        if input_type == "letter":
            guessed_letter = raw_input("What is your letter?")
            guessed_letter = guessed_letter.lower()
            
            while len(guessed_letter) > 1 or guessed_letter + " " in used:
                if len(guessed_letter) > 1:
                    guessed_letter = raw_input("You can only guess one letter:")
                else:
                    guessed_letter = raw_input("You already guessed that! Try again:")
                guessed_letter = guessed_letter.lower()

            else:
                used.append(guessed_letter + " ")
                if guessed_letter in answer:
                    index_list = []
                    for i in range(0,len(answer)):
                        if answer[i] == guessed_letter:
                            index_list.append(i)
                    for i in index_list:
                        j = i + 1
                        attempt[j] = guessed_letter + " "          
                else:
                    add_sequence()
                    guess += 1
	
	else:
            guessed_word = raw_input("What do you think the word is?")
            guessed_word = guessed_word.lower()

            if guessed_word == answer:
                attempt = list(answer)
            else:
                add_sequence()
                guess += 1



# Input: none
# Output: a boolean that is True if there are no blanks in 'attempt',
# meaning that the player has either filled in all the letters or
# guessed the word correctly; the output is false if there are blanks
# in 'attempt', indicating that there are still letters that are
# uknown to the player 
def word_match():
    return not ("__ " in attempt)




    
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~SECTION 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~ Game Loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


"""
This while/else loop is the actual game loop. It runs as long as the player
has not made max_guesses number of incorrect guesses, and as long as
'word_match' returns false. Once either of these conditions is not met,
the loop falls into an if-else clause that checks to see if the game is over
because the player won, or if it is over because the player ran out of
guesses. In either case, an appropriate message is displayed along
with the original word, which was stored in the 'answer' variable.
"""

while guess < max_guesses and (not word_match()):
    print_board(board)
    take_input()
else:
    if word_match():
        print "".join(answer)
        print "Congratulations! You won! The word was " + answer + "."
    else:
        print_board(board)
        print "You lost...the word was " + answer + ". Maybe try again?"

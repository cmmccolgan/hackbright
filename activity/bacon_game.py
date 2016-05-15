"""
Program: This is a game that will help you decide if you should eat bacon.
"""

# first set of questions
def is_like_angels(choice):
    if choice == 1:  # yes
        #sends user to the bottom of the function
        pass 
    elif choice == 2: # no
        print "You've clearly never eaten bacon."
    elif choice == 3: # maybe
        #pass to maybe condition function
        maybe_condition()
    #pass to eat_bacon function
    eat_bacon()

def maybe_condition():
    answer = raw_input("Are you a coward? Yes or No")
    if answer.lower() == "yes" or answer.lower() == "y":
        print "You are a coward." + "\n" + "Bacon will turn you into a true warrior"
    elif answer.lower() == "no" or answer.lower() == "n":
        print "You are not a coward."

#Pass to here:
def eat_bacon():
    print "Eat Some Bacon!"

#main function
def should_you_eat_bacon():
    #variable
    input_string = "Do you want to feel like angels are frolicking on your taste buds?" \
                   + "\n" + "1 - yes" + "\n" + "2 - no" + "\n" + "3 - yes, but I'm afraid it will kill me."

    #asking the question
    choice = int(raw_input(input_string))

   #following up on the users choice
   is_like_angels(choice)

#required to run the main function
if __name__ == '__main__':
    should_you_eat_bacon()


''' 
Program: This is a game that will help you decide if you should eat bacon.
'''
#FUNCTIONS:
#1st question
def is_like_angels(choice):
	if choice == 1:
		pass
	elif choice == 2:
		print "You've clearly never eaten bacon."
	elif choice == 3:
		maybe_condition()
	#Yes and no should show additional test
	eat_bacon()

#user selected yes or no they should also see this
def eat_bacon():
	print "Eat it!"
def maybe_condition():
	answer = raw_input("Are you a coward? Yes or No")
	if answer.lower() == "yes" or answer.lower() == "y":
		print "You are a coward." + "\n" + "Bacon will turn you into a true warrior"
	elif answer.lower() == "no" or answer.lower() == "n":
		print "You are not a coward."
#main function
def should_you_eat_bacon():
    #define variable options
    input_string = "Do you want to feel like angels are frolicking on your taste buds?"\
    				+ "\n" + "1 - Yes" \
    				+ "\n" + "2 - No" \
    				+ "\n" + "3 - Yes, but I'm afraid it will kill me."
    #define variable
    #asking user for input
    #typecast response to be a integer
    choice = int(raw_input(input_string))
	#following up on the users choice
    is_like_angels(choice)

#required to run the main function
if __name__ == '__main__':
    should_you_eat_bacon()

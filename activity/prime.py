'''
Python program to check if the input number is prime or not
'''

#USED FUNCITON
def ask_number():
	num = int(raw_input("Enter a number:"))
	return num 

def is_prime(user_input):
	if user_input == 0 or user_input == 1:
		return False
	for x in range(2, user_input):
		if user_input % x == 0:
			return False
	else:
		return True

def want_to_play():
	wanna_input = raw_input("Want to play again?").lower()
 	if wanna_input == "yes" or "y":
 		ask_number
 	else:
 		print "Thanks for playing"

#MAIN FUNCTION:
def prime_checker():
	#Ask the user for an integer input & Define as global variable
	user_input = ask_number()
	#Define users number prime status
	check_prime = is_prime(user_input)

	#Result for users input & Loop the user back
	while (check_prime == True):
		print "%i is prime!" %(user_input)
		break
	else:
		print "Your number is not prime :("
		want_to_play()

#Required for main
if __name__ == '__main__':
	prime_checker()
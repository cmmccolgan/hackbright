'''
PROJECT DESCRIPTION:
We are going to simulate a BART kiosk. 
BART has a smart card system called “Clipper” where riders can load money onto a smart card.
The smart card will keep track of the amount of money the rider has for train rides. 
When the card is used to pay for train rides and the cost of the ride is deducted. 
The rider does not need to have exact change for each train ride.
They can simply load a large sum of money onto the card and take as many rides as they want until the monetary amount on the card runs out.

dollar_1 =[1,2,3,4]
dollar_5 = [5]
dollar_10 = [10]
dollar_20 = [20]

#FUNCTIONS
def load_card(rider_balance,deposit):
	
	return 

#Argument 1:
print load_card(0,1.00)
#Argument 2:
print load_card(0,5.00)
#Argument 3:
print load_card(0,10.00)
#Argument 4:
print load_card(0,20.00)
'''
def changer(nominals, total):
	#Length of list
	used_nominals = [0] * len(nominals)
	for i, n in enumerate(nominals[::-1]):
		used_nominals[i] = total // n
		total -= used_nominals[i]*n
		return used_nominals, total

#def dict_changer(nominals, total): 
#	dict_nominals_count = {n: 0 for n in nominals} for n in nominals[::-1]: 
#	dict_nominals_count[n] = total // n total -= dict_nominals_count[n]*n 
#	return dict_nominals_count, total

def coin_changer(total):
  return changer([1,2],total)

def note_changer(total):
  return changer([5,10,20],total)

nominal_counts, left = changer([1,2,5,10,20], total)
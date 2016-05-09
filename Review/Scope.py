'''
Review Scope
'''
# Calculate how much to tip on the bill
def total_tip(tip_percent,new_bill):
	total_tip = tip_percent/100 * new_bill 
	return total_tip
# Calculate full bill price:
def total_bill(new_bill,total_tip):
	total_bill = new_bill + total_tip
	return total_bill
# Calculate individual price:
def split_bill(total_bill,split_amount):
	split_bill= total_bill/split_amount
	return split_bill
# ---------------------------------------------------------------------------------
def bill_calculator():	
	# What does the user want todo:
	print "What would you like to do:"
	print "1: Calculate Tip"
	print "2: Tip and Bill total including tip"
	print "3: Split Bill without tip"
	print "4: Split Bill with tip"
	print "5: Quit Application"
 	#Capture the menu choice.
	choice = int(raw_input())

	#User Selected 1
	if choice == 1:
		new_bill = float(raw_input("How much was your bill?"))
		tip_percent = float(raw_input("What percentage do you want to tip?"))
		tip = total_tip(tip_percent,new_bill)
		print "You wanted to tip %f percent therefore you should tip %f" %(tip_percent,tip)
	#User Selected 2
	elif choice == 2:
		new_bill = float(raw_input("How much was your bill?"))
		tip_percent = float(raw_input("What percentage do you want to tip?"))
		tip = total_tip(tip_percent,new_bill)
		bill = total_bill(new_bill,tip)
		print "You wanted to tip %f percent therefore you should tip %f" %(tip_percent,tip)
		print "Your total bill including tip is %f" %(bill)
	#User Selected 3
	elif choice == 3:
		new_bill = float(raw_input("How much was your bill?"))
		split_amount = int(raw_input("How many people do you want to split the bill?"))
		split = split_bill(new_bill,split_amount)
		print "Each of you should pay %f, this is without tip." %(split)
	#User Selected 4
	elif choice == 4:
		new_bill = float(raw_input("How much was your bill?"))
		tip_percent = float(raw_input("What percentage do you want to tip?"))
		split_amount = int(raw_input("How many people do you want to split the bill?"))
		tip = total_tip(tip_percent,new_bill)
		bill = total_bill(new_bill,tip)
		split = split_bill(bill,split_amount)
		print "You wanted to tip %f percent therefore you should tip %f" %(tip_percent,tip)
		print "Your total bill including tip is %f" %(bill)
		print "Each of you should pay %f" %(split)
	#User Selected 5
	elif choice == 5:
		print "Bye!"
		keepProgramRunning = False
	#Unclear what was choosen
	else:
		print "Please choose a valid option."
		print "\n"


#required for main
if __name__ == '__main__':
	bill_calculator()
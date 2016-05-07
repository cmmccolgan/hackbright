
'''
Thi program calculates the tip and the bill total.
The bill can also be split.

#Variables:
    #input by the user
        bill 
        tip_percentage
    
    #calculated by functions:
        calculate_tip
        calculate_bill_total
        calculate_split_bill

    #Show to user:
        tip 
        bill_total

'''
#functions
def calculate_tip(bill,tip_percentage):
	return bill * tip_percentage* .01

def calculate_bill_total(bill,tip):
	return bill + tip

def calculate_split_bill (bill_total, people):
	return bill_total/people

def main():
#Menu for the user to select what they want todo:    
    print "What would you like to do:"
    print "1: Calculate Tip"
    print "2: Bill and Tip Cost"
    print "3: Split Bill"
    print "4: Split Bill including tip"
    print "5: Quit Application"

    #Capture the menu choice.
    choice = int(raw_input())
    #if user selected #1 Calculate Tip
    if choice == 1:
        bill = float(raw_input("How much was your bill?"))
        tip_percentage = float(raw_input("What percentage would you like to tip?"))
        tip = calculate_tip(bill,tip_percentage)
        bill_total = calculate_bill_total(bill,tip)
        print "The tip is %f." % tip
    #if user selected #2 Bill and Tip Cost
    elif choice == 2:
        bill = float(raw_input("How much was your bill?"))
        tip_percentage = float(raw_input("What percentage would you like to tip?"))
        tip = calculate_tip(bill,tip_percentage)
        bill_total = calculate_bill_total(bill,tip)
        print "The tip is %f." % tip
        print "The bill total is %f." % bill_total
    #if user selected #3 Split the Bill
    elif choice == 3:
        bill = float(raw_input("How much was your bill?"))
        people = round(int(raw_input("How many people will be splitting the bill?")),2)
        split_amount = calculate_split_bill (bill, people)
        print "The bill is %f for each person." % (split_amount)
    #if user selected #4 Split Bill including tip
    elif choice == 4:
        bill = float(raw_input("How much was your bill?"))
        tip_percentage = float(raw_input("What percentage would you like to tip?"))
        people = round(int(raw_input("How many people will be splitting the bill?")),2)
        tip = calculate_tip(bill,tip_percentage)
        bill_total = calculate_bill_total(bill,tip)
        split_amount = calculate_split_bill (bill_total, people)
        print "The bill is %f for each person." % (split_amount)
    #if user selected #4 Quit Application
    elif choice == 5:
        print "Bye!"
        keepProgramRunning = False
    #user selected an invalid option
    else:
        print "Please choose a valid option."
        print "\n"

#Required to close & run main function
if __name__ == '__main__':
    main()
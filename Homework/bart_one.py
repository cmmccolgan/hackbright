def load_card(one_dollar_bills,five_dollar_bills,ten_dollar_bills,twenty_dollar_bills):
	#sum of all one dollar bills
	ones = one_dollar_bills * 1
	#sum of all five dollar bills
	fives = five_dollar_bills * 5
	#sum of all ten dollar bills
	tens = ten_dollar_bills * 10
	#sum of all twenty dollar bills
	twenties = twenty_dollar_bills * 20
	print "You entered %i $1 bills, %i $5 bills, %i $10 bills, and %i $20 bills" % (one_dollar_bills,five_dollar_bills,ten_dollar_bills,twenty_dollar_bills)
	return float(ones + fives + tens + twenties)

#Main Program =====================================================
def bart():
	print "Test Cases"
	#Test 1 - 0 $1 bills, 0 $5 bills, 0 $10 bills, and 0 $20 bills
	print load_card(0,0,0,0)  
	#Test 2 - 0 $1 bills, 0 $5 bills, 0 $10 bills, and 9 $20 bills
	print load_card(0,0,0,9)
	#Test 3 - 2 $1 bills, 3 $5 bills, 0 $10 bills, and 0 $20 bills
	print load_card(2,3,0,0)
	#Test 4 - 3 $1 bills, 1 $5 bill, 1 $10 bill, and 3 $20 bills
	print load_card(3,1,1,3)

#required to run main ============================================
if __name__ == '__main__':
	bart()



# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - fix this code :D
# (Part 1): Instead of using the hard coded ".18",
# Ask the user to input the percentage of tip they want to give. 
# Save the input to a variable. 
# Use the variable to calculate the tip.
# (Part 2): Fix any bugs and make it work!

# User provides inputs
bill = float(raw_input("How much was your bill?"))
tip = float(raw_input("What percentage do you want to tip?"))

# Calculate how much to tip on the bill 
total_tip = tip/100 * bill 

# Calculate full bill price:
total_bill = bill + total_tip

#Tell the user what you have done
print "The tip is %f and the total bill is %f ." % (total_tip, total_bill)

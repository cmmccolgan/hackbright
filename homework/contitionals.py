'''
#Conditionals #1
partner1 = "suraj"
partner2 = "cameron" 
if partner1 > partner2:
	print "My name is greater"
elif partner2 > partner1:
	print "Their name is greater"

#Conditionals #2
today = 24
end = 31

if today >= (end/2):
	print "Oh, we're more then half way to the end of the month"
elif today<= (end/2):
	print "This month is still young"

#Conditionls #3
today = "sun"
if today == "mon":
	print "Yay class day!"
elif today == "tue":
	print "Sigh, it's only Tuesday."
elif today == "wed":
	print "Humpday!" 
elif today == "thu":
	print "#tbt"
elif today == "fri":
	print "TGIF!"
elif today == "sat" or "sun":
	print "Yeah, it's the weekend!"

#Conditionals #4 
age = 20
if age >=18 and age >= 21:
	print "You can vote and go to the pub"
elif age >=18 and age <= 21:
	print "You can vote BUT you cannot go to the pub"
elif age >= 18:
	print "Yay! I can Vote!"
elif age <= 18:
	print "You have a few more years"

#Conditionals #5
number = 8
def isEven(number):
	return number%2 == 0
if number == isEven: 
	print "%i is even" %(number)
elif number != isEven:
	print "%i is odd" %(number)
'''
# Conditionals 6

num1 = 9
num2 = 9

def isEven(number):
        return number % 2 == 0

if isEven(num1):
	print "yes"
else:
	print "no"


if isEven(num1) and isEven(num2): 
	print "%i and %i is even" %(num1, num2)
elif isEven(num1) and not isEven(num2): 
	print "%i is even and %i is odd" %(num1, num2)
elif not isEven(num1) and isEven(num2): 
	print "%i is odd and %i is even" %(num1, num2)
elif not isEven(num1) and not isEven(num2):
	print "%i and %i is odd" %(num1, num2)

'''
#Conditionals 7

fav = "green"
if fav == "blue" or fav == "yellow" or fav == "red":
	print "My favorite color is a primary color!" 
else:
	print "My favorite color is a secondary color."

'''

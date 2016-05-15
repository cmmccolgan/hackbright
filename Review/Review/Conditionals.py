''' 
Reviewing conditionals

#CONDITIONAL EXERCISE 1
#1a
print 8 == 8

#1b
print 8 == "8"

#1c 
print 8 == 8.0

#2a
print "Cameron" == "Cameron"

#2b
print "cameron" != "Cameron"

#2c
print "cameron" > "Cameron"

#3a
print 9 < 8

#3b
print 9>=19

#3c
print 19<=9

#CONDITIONAL EXERCISE 2
#1
my_name = raw_input("What is your name?")
partners_name = raw_input("What is your name?")
if my_name > partners_name: 
	print " %s your name greater than %s name!" %(my_name, partners_name)
elif my_name == partners_name:
	print "Our names are the same!"
else:
	print "%s name is greater than %s" %(partners_name,my_name)

#2
users_date = int(raw_input("What day of the month is it?"))
if users_date>= 15:
	print "We are more than half way through the month"
else:
	print "The month is still young"	
'''

#3
user_weekday = raw_input("What day of the week is it?")
if user_weekday == "Monday":
	print "Yeah!! I have Coding Class"
elif user_weekday == "Tuesday":
	print "Ugh have to go to Mountain View"
elif user_weekday == "Wednseday":
	print "HUMP DAY and coding class"
elif user_weekday == "Thursday":
	print "Ugh back to Mountain View you go..."
elif user_weekday == "Friday":
	print "BOOM you made it to the end of the week!!!"
else:
	print "I guess it is the weekend for you!"















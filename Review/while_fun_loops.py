'''
Reviewing While Loops Lecture 10
'''

#1 PRINT OUT 1-20
#Start at 1 and not 0
# i = 1
# while (i<=20):
# 	#Print that Index
# 	print i,
# 	#Jump to next index and Repeat
# 	i+=1

#2 PRINT OUT 1-20 IF 13 PRINT HELLO
# index = 1
# while (index<=20):
# 	#If # is 13 print hello
# 	if index == 13:
# 		print "Hello"
# 	#otherwise print index
# 	else: 
# 		print index,
# 	# Repeat for the next index
# 	index+=1
#3 PRINT OUT 1-100 IN INCREMENTS OF 10
# index =1
# while (index <=101):
# 	if index % 10 == 0:
# 		print index
# 	index +=1
#4 List all contents of the list
fruits = ["apples", "oranges","banana"]
#Where to start counting
index=0

while (index<len(fruits)):
	#Want to print each fruit
	print fruits[index]
	#Jump to the next on the list
	index +=1




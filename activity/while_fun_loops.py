'''
GOAL is to use while loops

#?:1 Print out the numbers from 1 to 20.
i=0
while(i<21):
	print i
	i = i+1

#?:2 Print out the numbers from 1 to 20, 
i=0
while(i<21):
	if i == 13:
		print "hello"
	else:
		print i
	i = i+1
#?:3 print out the numbers from 1 to 20, 
i=0
while(i<101):
	if i%10 == 0:
		print i
	else:
		pass
	i = i+1

#?:4 Go through the list, and print out each fruit.
'''
fruit_list = ["apples", "oranges","bananas"]
i=0 

while (i < len(fruit_list)): #used to check length of the list
      print fruit_list[i] #prints out the fruit in the list
      i = i + 1 #Repeat for next index
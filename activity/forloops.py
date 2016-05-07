'''
#PART 1: 
for index in range(1,21):
	print index,

for index in range(1,21):
	if index == 13:
		print "hello"
	else:
		print index,
#PART 2: 
fruit_list= "apples","oranges", "bananas"

for fruit in fruit_list:
	print fruit

for index in range(len(fruit_list)):
	print (index, fruit_list[index])

#PART 3:
#Step 1 making sure we view the desired numbers
def sum_num(num):
	sum = 0
	for item in range(num):
		print item

sum_num(5)

#Step 2 adding all numbers
def sum_num(num):
	sum = 0
	for item in range(num):
		sum = sum + item
	return sum
total = sum_num(3)
print "total:", total
'''
#Step 3 include number itself
def sum_num(num):
	sum = 0
	for item in range(num+1):
		sum = sum + item
	return sum
total = sum_num(3)
print "Total:", total


'''
Review Loops
'''
#1 Print increments of 10: 
# for index in range(0,100,10):
#  	print index,

 #2 Print off numbers
# for index in range (1,10,2):
# 	print index,

 #3 print out number from 10 to 0
# for index in range(10,-1,-1):
# 	if (index==0):
# 		print "Blastoff!"
# 	else:
# 		print index,

#4 List 
#PART 3: PUTTING IT ALL TOGETHER ============================
# fruits =["apples","oranges","bananas"]

# #1 Not using range but using a loop print the list
# for fruit in fruits:
# 	print fruit
# #2 Using range print the list
# # for index in range(len(fruits)):
# # 	print fruits[index]

#3 Add All numbers up below the input number

# def sum_nums (num):
# 	#Where to start counting
# 	sum = 0
# 	#create the list we should add together
# 	for index in range(num):
# 		# add each index together
# 		sum += index
# 	#return the total	
# 	return sum

# print sum_nums(3)

#4 Add all numbers up below the input number including the number
# def sum_nums (num):
# 	#Where to start counting
# 	sum = 0
# 	#create the list we should add together including num
# 	for index in range(num+1):
# 		# add each index together
# 		sum += index
# 	#return the total	
# 	return sum

# print sum_nums(3)

#5 Check parameter is negative add all the negative numbers and return the sum. 
# If num is positive it should work the same

# def sum_nums2(num):
# 	#where to start counting
# 	sum =0
# 	#for negative numbers
# 	if (num<0):
# 		for index in range(0, num-1,-1):
# 			sum+= index
# 	#For positive numbers
# 	else:
# 		for index in range(num+1):
# 			sum += index
# 	return sum
# print sum_nums2(-3)
# print sum_nums2(9)
#6 print out 1-100 multiple of 3 print fizz, multiple of 5 print buzz, multiple of both fizzbuzz. 
def fizz_buzz(num):
	for index in range(num):
		if (index%3==0 and index%5==0):
			print "Fizzbuzz"
		elif (index%3==0):
			print "FIZZ"
		elif (index%5==0):
			print "BUZZ"
		else:
			print index,

print fizz_buzz(101)
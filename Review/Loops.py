'''
Review Loop
'''
#EXERCISE 1 ----------------------------------
# print "1", range (5)
# print "2", range (3.14) #Fail decimals are not accepted
# #Empty print "3", range(-8)
# #Empty print "4", range(0)
# print "5", range (1)
# print "6", range(1,5)
# #Empty print "7", range (5,1)
# print "8", range (5,1,-1)

#EXERCISE 2 ----------------------------------
#Understanding Range:
#print range (1,21)
#1
#for index in range(1,21):
#	print index,
#2
# for index in range(1,21):
	# if (index == 13):
	# 	print "Hello"
	# else:
	# 	print index,

#EXERCISE 3 -----------------------------------
# fruits = "apples", "bananas", "oranges"
# #1a
# for fruit in fruits:
# 	print fruit
# #1b
# for i in range(len(fruits)):
# 	print fruits[i]

#2
# def sum_nums (num):
# 	sum =0
# 	for index in range (num):
# 		sum+= index
# 		return sum

# print sum_nums(3)

#EXERCISE 4 -----------------------------------
def fizz_buzz(num):
	#We want to count to 100 and print each index
	for index in range(num):
		#If number is divisible by 3 and 5 - print FIZZBUZZ
		if index % 3 ==0 and index % 5 ==0:
			print "FIZZBUZZ"
		#If number is divisible by -  print FIZZ
		elif index % 3 ==0:
			print "FIZZ"
		#If number is divisible by 5 - print BUZZ
		elif index % 5 ==0:
			print "BUZZ"
		# print index
		else:
			print index
	
print fizz_buzz(101)
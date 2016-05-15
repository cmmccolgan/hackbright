'''
Review Functions

#EXERCISE 1 -------------------------------------

#VARIABLES
name = "Katsup"

#1 prints hello
def hello_print():
	print "hello"

#2 returns hello
def hello_return():
	return "hello"

#3 prints hello and uses parameter
def hello_name(name):
	print "hello", name

# CALLING FUNCTIONS
print "Number 1", hello_print()
print "Number 2", hello_return()
print "Number 3", hello_name(name)

'''
#EXERCISE 2 -------------------------------------
#1
def addition(num1,num2):
	add_total = num1+num2
	return add_total
#2
def subtract(num1,num2):
	sub_total = num1-num2
	return sub_total
#3
def multiply(num1,num2):
	mul_total = num1*num2
	return mul_total
#4
def divide(num1,num2):
	div_total=num1/num2
	return div_total
#5
def modulo(num1,num2):
	mod_total=num1%num2
	return mod_total
#6
def power(num1,exponent):
	pow_total=num1**exponent
	return pow_total
#7
def square (num1,exponent):
	squ_total=num1**2
	return squ_total
#TESTING FUNCTIONS:
print "addition 4+5=", addition(4,5)
print "subtract 10-5=", subtract(10,5)
print "multiply 5*2=", multiply(5,2)
print "divide 110/2=", divide(110,2)
print "modulo 10*3=", modulo(10,3)
print "power 5**5=", power(5,5)
print "square 5**2=", square(5,2)

#8
print "8a", addition(addition(4,5),subtract(9,6))
print "8b", subtract(divide(12,2),60)
print "8c", addition(addition(1,2),3)
print "8d", power(addition(1,2),2)
print "8e", divide(modulo(3,4),multiply(9,9))
print "8f", multiply(7,addition(3,8))
print "8g", multiply(subtract(addition(1,2),3), addition(4,5))
print "8h", power(3,addition(2,3))
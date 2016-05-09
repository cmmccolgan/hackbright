#Functions Activity 2

#functions ----------------------------------------------
def add(num1,num2):
	return num1 + num2

def subtract(num1,num2):
	return num1 - num2

def multiply(num1,num2):
	return num1 * num2

def divide(num1,num2):
	return num1/num2

def modulo(num1,num2):
	return num1%num2

def power(base,exponent):
	return base**exponent

def square(num):
	return power(num,2)
'''
#variables ----------------------------------------------
num1=8
num2=8
base=4
exponent=5
num=10

#confirm function behavior --------------------------------
print "Add" 
print add(num1,num2)

print "Subtract" 
print subtract(num1,num2)

print "Multiply" 
print multiply(num1,num2)

print "Divide" 
print divide(num1,num2)

print "Modulo" 
print modulo(num1,num2)

print "Power" 
print power(base,exponent)

print "Square" 
print square(num)
'''
#Exercise Assignment ----------------------------------------------
print "1. (4+5) + (9-6)"
print add(add(4, 5),subtract(9, 6))
print "2. (12/2) - 60"
print subtract(divide(12, 2), 60)
print "3. 1 + 2 + 3"
print add(add(1, 2), 3)
print "4. (1 + 2)2"
print square(add(1, 2))
print "5. (3%4) / 9*9"
print divide(modulo(3, 4), multiply(9,9))
print "6. 7 * (3+8)"
print multiply(7, add(3, 8))
print "7. (1+2) - 3 * (4+5)"
print subtract(add(1, 2), multiply(3, add(4, 5)))
print "8. 3^(2+3)"
print power(3, add(2, 3))



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
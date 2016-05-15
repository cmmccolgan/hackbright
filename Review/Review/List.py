'''
Reviewing list lecture
'''

my_list = [1,2,"kitten",4,"five",6,7]
#EXERCISE 1 ----------------------------------------
# #1
# print my_list[2]
# #2 
# print my_list[3]
# #3 
# print my_list[1]
# #4 3 ways to access last element
# print my_list[4]
# print my_list[-1]
# print my_list[4:]
# print my_list[4:5]
# #5 Shows number of items in the list
# print len(my_list)

#EXERCISE 2 ---------------------------------------
"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.

shopping_list = []

def add_shopping_list(item):
	#Force lower case
    item = item.lower()
    #Check if item is in shopping list
    if item not in shopping_list:
        #Add item to the end of the list
        shopping_list.append(item)
        #print "Here's your updated list", sorted_shopping_list()
    else:
        print "This item %s already exists!" % (item)

def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list

def remove_item(item):
	#Force lower case
    item = item.lower()
    #Check if item is in shopping list
    if item in shopping_list:
        #remove item from list
        shopping_list.remove(item)
        #print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    else:
        print "%s was not on the list." % (item)

def replace_item(old_item, new_item):
	#Force lower case
    old_item = old_item.lower()
    new_item = new_item.lower()
    #Check if item is in shopping list
    if old_item in shopping_list:
        #check existing list for item
        item_index = shopping_list.index(old_item)
        shopping_list.remove(old_item)
        shopping_list.append(new_item)
        #print "%s has replaced %s in the list." % (new_item, old_item)

    else:
        print "%s is not in the list." % (old_item)

# MAIN Program 
def shopping_time():
	#CHECK - add_shopping_list Function
	add_shopping_list("apple")
	add_shopping_list("steak")
	add_shopping_list("beef")
	add_shopping_list("mustard")
	#CHECK - remove_item Function
	remove_item("apple")
	#CHECK - replace_item Function
	replace_item("mustard", "ketchup")

	print shopping_list
#Required for MAIN program 
if __name__ == '__main__':
	shopping_time()
"""

#EXERCISE 3 --------------------------------------------------------------
prime_list = [ ]

def primes():
    yield 2
    n = 2
    while True:
        n + =1
        for p in primes():
            if (n % p) == 0:
                prime_list.add(n)
        else:
            yield n

print primes(4)


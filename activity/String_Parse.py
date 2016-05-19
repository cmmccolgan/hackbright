# #1 =================================================
# my_name = "cameron"
# print list(my_name)

#2 =================================================
# #original List
# num_str = "1,2,3,4,5" 
# # remove comma
# split_num.split(",")
# # Create new list
# new_list =[]
# # Convert string to int
# for items in split_num:
# 	items = int(item)
# 	#add int to new list
# 	new_list.push(items)
	
# print new_list

#3 =================================================
# seuss = "One fish two fish red fish blue fish"
# # Remove fish
# seuss = seuss.split(" fish")
# #Remove Space
# seuss.pop()
# print seuss

#4 =================================================

def format_string (str_input):
	split_str =str_input.split(",")
	quantity = float (split_str[1].split(";")[1])
	price = float (split_str[2].split(";")[2])
def calculate_bill(tuple):
	quantity = tuple_input[0]
	price = tuple_input[1]
	return quantity * price

items = ["item:apples,quantity:4,price:1.50\n",
"item:pears,quantity:5,price:2.00\n",
"item:cereal,quantity:1,price:4.49\n"]
#how to count them
total = 0
for item in items:
	#breakout each string & calculate how much each string cost
	grocery_bill = calculate_bill(format_string(item))
	# add each item to the total
	total += grocery_bill

print total
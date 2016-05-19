'''
Code Appetizer
'''
food_price_tuple = ('sushi',7.50,'burrito',8.20,'cheeseburger',6.00,'hot dog', 3.40,'fried rice', 9.99)
		
# main function ======================================
def convert_tuple_to_dic(tuple):
	item_index =0
	Global
	food_dictionary={}
	for item in tuple:
		if item_index %2 ==0:
			food_dictionary[item]= tuple[index+1]
		item_index +=1

	return food_dictionary

#food_dictionary = convert_tuple_to_dic(food_price_tuple)

#test function
print food_dictionary
print food_dictionary['sushi']



# # Required to run main
# if __name__ == '__main__':
# 	convert_tuple_to_dic()
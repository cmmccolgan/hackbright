'''
'''
#Functions
def add_element(item):
	todo_list.append(item)
	return todo_list

def delete_element(item):
	todo_list.remove(item)
	return todo_list

def list_element(item):
	todo_list.sort(item)
	return todo_list
#List
todo_list = []

#main element
def todo():
	print add_element("grapes")
	print add_element("milk")
	print add_element("oranges")
	print delete_element("pickles")
	print delete_element("milk")
	print list_element()
#required for main
if __name__ == '__main__':
	todo()
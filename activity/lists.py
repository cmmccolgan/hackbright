'''
This exercise is to solidify the List presentation
'''
#STARTING EXAMPLE YOU SHOULD BUILD OFF OF
class_room = ["Chair","projector"]
print class_room

#THREE WAYS TO ADD 2 ITEMS TO THE LIST
#1st
class_room = class_room + ["pcs","snacks"]
print class_room
#2nd
class_room.append("pc")
class_room.append("snacks")
print class_room
#3rd
class_room.extend("pc","snacks")
print class_room

#THREE WAYS TO REMOVE 2 ITEMS TO THE LIST
#1st
del class_room[1]
print class_room
#2nd
class_room.remove("Chair")
print class_room
#3rd
class_room.remove(class_room[1])
print class_room

#REMOVE THE ITEM 'SNACKS'
#1st
class_room.remove("Snacks")
print class_room
#2nd
class_room.pop()
print class_room
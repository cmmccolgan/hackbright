
#Lecture =============================================== 
#Your given a string
str = "item:apples,quantity:4,price:1.50\n"
#Remove Comma
split_str= str.split(",")
# Grab index 1 and remove colan
quantity = split_str[1].split(":")[1]
# Grab index 2 and remove colan
price = split_str[2].split(":")[1]
# convert string to float and remove n/ aswell
quantity = float(quantity)
price = float(price)
#Test current values
print quantity
print price

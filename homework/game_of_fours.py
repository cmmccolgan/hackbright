#loop method
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
#recursive method
'''def factorial(n):
	if n == 1
		return 1;
	return n * factorial(n-1)
'''
#0 ---------------------------------------------------------------------
zero_string = "44-44"
print "%s = %i" % (zero_string, eval(zero_string))
one_string = "44/44"
print "%s = %i" % (one_string, eval(one_string))
two_string = "(4*4)/(4+4)"
print "%s = %i" % (two_string, eval(two_string))
three_string = "(4*4-4)/4"
print "%s = %i" % (three_string, eval(three_string))
four_string = "((4-4)*4)+4"
print "%s = %i" % (four_string, eval(four_string))
five_string = "(4**2+(4**2/4))/4"
print "%s = %i" % (five_string, eval(five_string))
six_string = "4-4+(factorial(4)/4)"
print "%s = %i" % (six_string, eval(six_string))
seven_string = "44/4-4"
print "%s = %i" % (seven_string, eval(seven_string))
eight_string = "4+4+4-4"
print "%s = %i" % (eight_string, eval(eight_string))
nine_string = "(4/4)+4+4"
print "%s = %i" % (nine_string, eval(nine_string))
# 10 -------------------------------------------------------------------
ten_string = "(factorial(4)/4)+(4**2/4)"
print "%s = %i" % (ten_string, eval(ten_string))
eleven_string = "44/(4**2/4)"
print "%s = %i" % (eleven_string, eval(eleven_string))
twelve_string = "4+4+(4**2/4)"
print "%s = %i" % (twelve_string, eval(twelve_string))
thirteen_string = "4**2-4+(4/4)"
print "%s = %i" % (thirteen_string, eval(thirteen_string))
fourteen_string = "44-factorial(4)-factorial(4)/4"
print "%s = %i" % (fourteen_string, eval(fourteen_string))
fifteen_string = "(44/4)+4"
print "%s = %i" % (fifteen_string, eval(fifteen_string))
sixteen_string = "4+4+4+4"
print "%s = %i" % (sixteen_string, eval(sixteen_string))
seventeen_string = "(44+factorial(4))/4"
print "%s = %i" % (seventeen_string, eval(seventeen_string))
eighteen_string = "(4**2)+(factorial(4)/4)-4"
print "%s = %i" % (eighteen_string, eval(eighteen_string))
nineteen_string = "factorial(4)-4-(4/4)"
print "%s = %i" % (nineteen_string, eval(nineteen_string))
# 20 -------------------------------------------------------------------
twenty_string = "44-factorial((4**2)/4)"
print "%s = %i" % (twenty_string, eval(twenty_string))
twentyone_string = "factorial(4)-4+(4/4)"
print "%s = %i" % (twentyone_string, eval(twentyone_string))
twentytwo_string = "factorial(4)-(factorial(4)/4)+4"
print "%s = %i" % (twentytwo_string, eval(twentytwo_string))
twentythree_string = "factorial(4)-(4**2/(4*4))"
print "%s = %i" % (twentythree_string, eval(twentythree_string))
twentyfour_string = "4*4+4+4"
print "%s = %i" % (twentyfour_string, eval(twentyfour_string))
twentyfive_string = "factorial(4)+(4**2/(4*4))"
print "%s = %i" % (twentyfive_string, eval(twentyfive_string))
twentysix_string = "(factorial(4)/4)+4**2+4"
print "%s = %i" % (twentysix_string, eval(twentysix_string))
twentyseven_string = "factorial(4)+4-(4/4)"
print "%s = %i" % (twentyseven_string, eval(twentyseven_string))
twentyeight_string = "4+4+4+4**2"
print "%s = %i" % (twentyeight_string, eval(twentyeight_string))
twentynine_string = "factorial(4)+4+(4/4)"
print "%s = %i" % (twentynine_string, eval(twentynine_string))
#  30 -------------------------------------------------------------------
thirty_string = "(factorial(4**2/4))+(factorial(4)/4)"
print "%s = %i" % (thirty_string, eval(thirty_string))
thirtyone_string = "4**2+4**2-(4/4)"
print "%s = %i" % (thirtyone_string, eval(thirtyone_string))
thirtytwo_string = "factorial(4)+4+(4**2/4)"
print "%s = %i" % (thirtytwo_string, eval(thirtytwo_string))
thirtythree_string = "4**2+4**2+(4/4)"
print "%s = %i" % (thirtythree_string, eval(thirtythree_string))
thirtyfour_string = "factorial(4)+(factorial(4)/4)+4"
print "%s = %i" % (thirtyfour_string, eval(thirtyfour_string))
thirtyfive_string = "(factorial(4)/4)**2-(4/4)"
print "%s = %i" % (thirtyfive_string, eval(thirtyfive_string))
thirtysix_string = "44+4**2-factorial(4)"
print "%s = %i" % (thirtysix_string, eval(thirtysix_string))
thirtyseven_string = "(factorial(4)/4)**2+(4/4)"
print "%s = %i" % (thirtyseven_string, eval(thirtyseven_string))
thirtyeight_string = "4**2+4**2+(factorial(4)/4)"
print "%s = %i" % (thirtyeight_string, eval(thirtyeight_string))
thirtynine_string = "4**2+factorial(4)-(4/4)"
print "%s = %i" % (thirtynine_string, eval(thirtynine_string))
#  40 -------------------------------------------------------------------
forty_string = "4**2+factorial(4)+4-4"
print "%s = %i" % (forty_string, eval(forty_string))
fortyone_string = "(4/4)+4**2+factorial(4)"
print "%s = %i" % (fortyone_string, eval(fortyone_string))
fortytwo_string = "factorial(4)+factorial(4)-(factorial(4)/4)"
print "%s = %i" % (fortytwo_string, eval(fortytwo_string))
fortythree_string = "44-(4/4)"
print "%s = %i" % (fortythree_string, eval(fortythree_string))
fortyfour_string = "(4*44)/4"
print "%s = %i" % (fortyfour_string, eval(fortyfour_string))
fortyfive_string = "(4/4)+44"
print "%s = %i" % (fortyfive_string, eval(fortyfive_string))
fortysix_string = "factorial(4)+4**2+(factorial(4)/4)"
print "%s = %i" % (fortysix_string, eval(fortysix_string))
fortyseven_string = "factorial(4)+factorial(4)-(4/4)"
print "%s = %i" % (fortyseven_string, eval(fortyseven_string))
fortyeight_string = "(factorial(4)/4)*4+factorial(4)"
print "%s = %i" % (fortyeight_string, eval(fortyeight_string))
fortynine_string = "factorial(4)+factorial(4)+(4/4)"
print "%s = %i" % (fortynine_string, eval(fortynine_string))
#  50 -------------------------------------------------------------------
fifty_string = "44+(factorial(4)/4)"
print "%s = %i" % (fifty_string, eval(fifty_string))
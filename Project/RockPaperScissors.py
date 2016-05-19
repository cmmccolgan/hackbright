from random import choice
# Ask the User for their name
name = raw_input("Enter your name: ")
#Make sure they know the rules
print "Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock"
# How to score them
rps = ['r','p','s']
#User Score
u = 0
# Computer Score
v = 0

while 1:
    #Show them how to input their choice
    print "R: Rock,      P: Paper,     S: Scissor"
    
    #User's Choice
    user = raw_input("Enter your choice: ")   
    #only consider lower case
    user = user.lower()
    
    #Computer's Choice
    py = choice(rps)

#TIE
    if user == py:
        print "You chose", user , "and I chose", py
        print "TIE"

#User Wins
    #ROCK/SCISSORS
    elif user == 'r' and py == 's':
        print "You Win!!! Your Rock crushed my Scissors."
        u = u+1
    #PAPER/ROCK
    elif user == 'p' and py == 'r':
        print "You Win!!! Your Paper smothered my Rock."
        u = u+1
    #SCISSORS/PAPER
    elif user == 's' and py == 'p':
        print "You Win!!! Your Scissors chopped up my Paper."
        u = u+1

#Computer wins
    #ROCK/PAPER
    elif user == 'r' and py == 'p':
        print "You Lose!!! My Paper suffocated your Rock."
        v = v+1
    #PAPER/SCISSORS
    elif user == 'p' and py == 's':
        print "You Lose!! My Scissors sliced your Paper."
        v = v+1
    #SCISSORS/ROCK
    elif user == 's' and py cd== 'r':
        print "You Lose!! My Rock pummeled your Scissor."
        v = v+1
    
    #Computer Won Round
    if v == 3:
        #Print computer wins the game
        print "Sorry",name,"your the loser"
        break
    #User Won Round
    elif u == 3:
        #Congratulate the user on winning along with their name
        print "Congrats",name,"your the WINNER!!!"
        break
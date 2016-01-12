# Pig Game
# Nov 17, 2015
# adapted from here: http://cs.gettysburg.edu/projects/pig/piggame.html


import random

def humanOneTurn(theCurrentPlayerScore):
    turnSum = 0
    isStillRolling = True
    while isStillRolling == True:
        theRoll = random.randint(1,6)
        print("Roll: " + str(theRoll) )
        turnSum = turnSum + theRoll
        if theRoll == 1:
            turnSum = 0
            isStillRolling = False
        else:
            print("Turn total: " + str(turnSum) + "  Roll/Hold?")
            theChoice = input("Roll/Hold?")
            if theChoice != "": #they are holding
                isStillRolling = False

    theCurrentPlayerScore = theCurrentPlayerScore + turnSum
    print("Turn total: " + str(turnSum) )
    return theCurrentPlayerScore

def oneTurn(theCurrentPlayerScore, amountToStopAt):
    '''Roll until either get to amountToStopAt points, win the game (get to more than 100 points), or lose by rolling a 1.'''
    turnSum = 0
    isStillRolling = True
    while isStillRolling:
        theRoll = random.randint(1,6)
        turnSum = turnSum + theRoll
        print("Roll: " + str(theRoll) )
        if theRoll == 1:    #got nothing this turn
            turnSum = 0
            isStillRolling = False
        elif theCurrentPlayerScore + turnSum >= 100:    #stop, because you win!
            isStillRolling = False
        elif turnSum >= amountToStopAt: #stop because had a good turn
            isStillRolling = False

    theCurrentPlayerScore = theCurrentPlayerScore + turnSum
    print("Turn total: " + str(turnSum) )
    #print("New score: " + str(theCurrentPlayerScore))
    return theCurrentPlayerScore


player1Score = 0
player2Score = 0
whoseTurn = 1

while player1Score < 100 and player2Score < 100:    #nobody has won yet
    print("Player 1 score: " + str(player1Score) )
    print("Player 2 score: " + str(player2Score) )
    print("It is player " + str(whoseTurn) + "'s turn.")

    if whoseTurn == 1:
        player1Score = humanOneTurn(player1Score)
        whoseTurn = 2
    else:
        player2Score = oneTurn(player2Score, 20)
        whoseTurn = 1

print("Game over!")
print("Player 1 score: " + str(player1Score) )
print("Player 2 score: " + str(player2Score) )

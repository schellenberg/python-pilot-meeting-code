#-------------------------------------------------------------------------------
# Name:        Number Guessing Game
# Purpose:     To have a bit of fun, and demo some basic Python.
#
# Author:      Dan Schellenberg
#
# Created:     06/10/2015
# Copyright:   (c) SchellenbergD 2015
# Licence:     <your licence>
#
# As a WMCI Computer Science student, I state on my honour that I will:
# - cite any help that I have received (from other students, forums, etc.) on this assignment
# - not share actual program code with others. I realize that I am ENCOURAGED to discuss my approaches to solving problems, but that I should not share actual code.
# - be ready to explain any parts of the code I submit. I know that if I don’t understand what something does, it doesn’t belong in my assignment.
#-------------------------------------------------------------------------------

import random
computerNumber = random.randint(1,100)

userNumber = input("Please guess a number:")
userNumber = int(userNumber)    #converting from str to int

while userNumber != computerNumber:
    if userNumber > computerNumber:
        print("That's too high. Try again.")
    else:
        print("That's too low. Try again.")

    userNumber = input("Please guess a number:")
    userNumber = int(userNumber)    #converting from str to int

print("Way to go! You got it!")


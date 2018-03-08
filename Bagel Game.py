#Bagel Game 
import random


Num_Digits = 3
Max_Guess = 10
#Returns a string of unique random digits that is Num_Digits long
def secretNum():
    numbers= list(range(10))
    random.shuffle(numbers)
    secretNum= ""
    for i in range(Num_Digits):
        secretNum += str(numbers[i])
        ''' secretNum= secretNum+string numbers of i) '''
        return secretNum
#Returns a string with the Pico, Fermi, & Bagles cluse to the user 
def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it!"

    clues= [ ]
    for i in range(len(guess)):
        if guess[i] == secretNum [i]:
            clues.append("Fermi")
        elif guess [i] in secretNum:
            clues.append("Pico")
    if len(clues)==0:
             return "Bagles"

    clues.sort()
    return "".join(clues)
#Returns true if num is a string of only digits. Otherwise returns true or false
def isOnlyDigits(num):
    if num== "":
        return False

    for i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False
        return True
print("I am thinking of a %s- digit number. Try to guess what it is." %(Num_Digits))
print("The clues I give are...")
print("When I say:          That means:")
print("Bagles               None of the digits are correct")
print("Pico                 One of the digits is correct but in the wrong order")
print("Fermi                One digit is correct and in the right position")

while True:
    secretNum= getSecretNum=()
    print("I have thought up a number. You have to %s guesses to get it." %(Max_Guess) )

    guessesTaken = 1
    while guessesTaken <= Max_Guess:
        guess = ""
        while len(guess) != Num_Digits or not isOnlyDigitis(guess):
            print("guess #%s: " % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > Max_Guesses:
            print("You have ran out of guesses. The answer was %s." %(secretNum))

    print("Do you want to play again? (yes or no)")
    if not input().lower90.startswitch("Y"):
        break

          

    

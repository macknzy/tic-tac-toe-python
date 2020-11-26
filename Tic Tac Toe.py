#game setup
import random
import sys
import time
pastmoves = ["1","2","3","4","5","6","7","8","9"]
pastmoves1 = ["1","2","3","4","5","6","7","8","9"]
move = 0
botornobot = 0
score = int(0)
user = 0
botuser = 0
move1 = 0
move2 = 0


#before game questions and info
tempbotornobot = input("Would you like to play with a bot or in 2 player mode (y/n)?: ")
if tempbotornobot == "y":
    botornobot = 1
if tempbotornobot == "n":
    botornobot = 0
tempuser = input("Player 1: would you like to be X or O?: ")
if tempuser == "x":
    user = "X"
    botuser = "O"
if tempuser == "o":
    user = "O"
    botuser = "X"


#defining global functions
 
#board
def board():
    print("     |     |     \n ",pastmoves[6]," | ",pastmoves[7]," | ",pastmoves[8],"  \n_____|_____|_____\n     |     |     \n ",pastmoves[3]," | ",pastmoves[4]," | ",pastmoves[5],"  \n_____|_____|_____\n     |     |     \n ",pastmoves[0]," | ",pastmoves[1]," | ",pastmoves[2],"  \n     |     |     ")


#winner checker
def winnercheck():
    if pastmoves[6] == pastmoves[7] == pastmoves[8]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[3] == pastmoves[4] == pastmoves[5]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[0] == pastmoves[1] == pastmoves[2]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[6] == pastmoves[3] == pastmoves[0]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[7] == pastmoves[4] == pastmoves[1]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[8] == pastmoves[5] == pastmoves[2]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[6] == pastmoves[4] == pastmoves[1]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)
    if pastmoves[0] == pastmoves[4] == pastmoves[8]:
        score = 1
        board()
        print("You win!")
        time.sleep(60)


#making sure number is in range
def numcheck():
    while move > 9:
        print("This was not an option!")
def numcheck1():
    while move1 > 9:
        print("This was not an option!")
def numcheck2():
    while move2 > 9:
        print("This was not an option!")


#playing with a bot
def playwithbot():
    
    
    #computer response setup
    def bot():
        botmove = random.randint(0 ,8)
        while pastmoves[botmove] == user:
            botmove = random.randint(0 ,8)
        pastmoves[botmove] = botuser


    #user playing the game
    board()
    while score == 0:
        move = int(input("Where would you like to go (1-9)?: "))
        numcheck()
        pastmoves[move-1] = user
        winnercheck()
        bot()
        board()
        winnercheck()


#play with no bot
def playwithnobot():
    

    #defining second board
    def board1():
        print("     |     |     \n ",pastmoves1[6]," | ",pastmoves1[7]," | ",pastmoves1[8],"  \n_____|_____|_____\n     |     |     \n ",pastmoves1[3]," | ",pastmoves1[4]," | ",pastmoves1[5],"  \n_____|_____|_____\n     |     |     \n ",pastmoves1[0]," | ",pastmoves1[1]," | ",pastmoves1[2],"  \n     |     |     ")


     #user playing the game
    board1()
    while score == 0:
        move1 = int(input("Player 1: where would you like to go (1-9)?: "))
        pastmoves1[move1-1] = user
        numcheck1()
        winnercheck()
        while pastmoves1[move1-1] == "x" or pastmoves1[move1-1] == "o":
            move1 = int(input("Player 1: that square was already taken! where would you like to go (1-9)?: "))
        winnercheck()
        board1()

        move2 = int(input("Player 2: where would you like to go (1-9)?: "))
        pastmoves1[move2-1] = botuser
        numcheck2()
        winnercheck()
        while pastmoves1[move1-1] == "x" or pastmoves1[move1-1] == "o":
            move2 = int(input("Player 2: that square was already taken! where would you like to go (1-9)?: "))
        winnercheck()
        board1()


#finished
if botornobot == 1:
    playwithbot()
if botornobot == 0:
    playwithnobot()
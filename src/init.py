from classes import *

#Initializing Carrom Game
def initializeGame():
    numberOfBlackCoins = 9
    numberOfRedCoins = 1
    coins = CarromCoins(numberOfBlackCoins,numberOfRedCoins)

    player1 = Players( input("Enter first player's name: ") or "noob1")
    player2 = Players( input("Enter second player's name: ") or "noob2")
    #player3 = Players( input("Enter third player's name: ") or "noob3" )

    return CarromGame(coins,[player1,player2])
from classes import *

def getAllScoresAndPlayers(carrom):

    print(type(carrom.players))

    return tuple(sorted(carrom.players,key=lambda x: x.score))

def printScore(players):

    for player in players:

        print( "{0}\t score: {1}".format(player.name,player.score) )


def printCoinStatus(coins):

    print("Black Coins Left: {0}\t Red Coins Left: {1}".format(coins.numberOfBlackCoins,coins.numberOfRedCoins))


def checkResult(carrom):

    printCoinStatus(carrom.coins)

    players = getAllScoresAndPlayers(carrom)

    printScore(players)

    if( players[-1].score >= 5 and ( players[-1].score - players[-2].score  ) >= 3   ):
        print( "{0} won the game ".format(players[-1].name) )
        return True
    
    if( carrom.coins.numberOfBlackCoins == 0 and carrom.coins.numberOfRedCoins == 0 ):

        if( players[-1].score >= 5 or ( players[-1].score - players[-2].score  ) >= 3):
            print( "{0} won the game ".format(players[-1].name) )
            return True
        else:
            print("All Coins Exhausted!! Game Drawn")
            return True
    return False  
    

def playGame(carrom):

    message = "Choose an option from below "
    total_players= len(carrom.players)
    print("Total Players: ",total_players)

    while True:

        for player in range(total_players):

            while True:

                print( "{0}: {1}".format(carrom.players[player-1].name,message) )
                carrom.printGameOptions()

                try:

                    option = int(input())
                
                except:
                    print("Please enter a valid input ")
                    continue


                if( option == 1 ):
                    if( not carrom.strike(player-1) ):
                        print("No more black coins available on board")
                        continue
                    break
                elif( option == 2 ):
                    if( not carrom.multiStrike(player-1) ):
                        print("Less than 2 black coins available on board")
                        continue
                    break
                elif( option == 3 ):
                    if ( not carrom.redStrike(player-1) ):
                        print("No more red coins available on board")
                        continue
                    break
                elif(option == 4 ):
                    carrom.strikerStrike(player-1)
                    break
                elif( option == 5 ):
                    coin_type = input("Which coin is defuncted? red or black?").lower()
                    if(coin_type == "red" or coin_type == "black"):
                        if( not carrom.defunct(player-1,coin_type) ):
                            print("No {0} coins available".format(coin_type))
                            continue
                        break
                    else:
                        print("Coin type should be red or black")
                        continue
                elif( option == 6 ):
                    carrom.noneStrike(player-1)
                    break
            
            if( checkResult(carrom) ):
                return

numberOfBlackCoins = 9
numberOfRedCoins = 1
coins = CarromCoins(numberOfBlackCoins,numberOfRedCoins)

player1 = Players("Sachin")
player2 = Players("Dhoni")



carrom = CarromGame(coins,[player1,player2])

print(dir(carrom.players))

playGame(carrom)


def getAllScoresAndPlayers(carrom):

    return tuple(sorted(carrom.players,key=lambda x: x.score))

'''def getScores(players):

    scores = []

    for player in players:

        scores.append("{0} : {1}".format(player.name,player.score) )

    return scores'''

def getCoinStatus(coins):

    return "Black Coins Left: {0}\tRed Coins Left: {1}".format(coins.numberOfBlackCoins,coins.numberOfRedCoins)

def checkWinner(players):

    if( players[-1].score >= 5 and ( players[-1].score - players[-2].score  ) >= 3   ):
        
        return (True, players[-1].name)
    else:
        return (False, None)

def checkWinnerIfCoinNotAvailable(players):
    
    if( players[-1].score >= 5 or ( ( players[-1].score - players[-2].score  ) >= 3 ) ):
        return (True, players[-1].name)
    else:   
        return (True,None)


def checkResult(carrom):

    print(getCoinStatus(carrom.coins),end="\n")

    players = getAllScoresAndPlayers(carrom)

    for player in players: print("{0} : {1}".format(player.name,player.score))

    status,winner = checkWinner(players)

    if(status):
        return (status,winner)
    
    if( carrom.coins.numberOfBlackCoins == 0 and carrom.coins.numberOfRedCoins == 0 ):

        return checkWinnerIfCoinNotAvailable(players) 
    
    return (False,None)  
    

def playGame(carrom):

    message = "Choose an option from below\n"
    total_players= len(carrom.players)
    print("Total Players: ",total_players)

    while True:

        for player in range(total_players):

            while True:

                print( "{0}: {1}".format(carrom.players[player].name,message) )
                carrom.printGameOptions()

                try:

                    option = int(input())

                except KeyboardInterrupt:
                    exit("Exiting......")
                
                except EOFError:
                     exit("Exiting......")
                
                except:
                    print("Please enter a valid input \n")
                    continue


                if( option == 1 ):
                    if( not carrom.strike(player) ):
                        print("No more black coins available on board\n")
                        continue
                    break
                elif( option == 2 ):
                    if( not carrom.multiStrike(player) ):
                        print("Less than 2 black coins available on board\n")
                        continue
                    break
                elif( option == 3 ):
                    if ( not carrom.redStrike(player) ):
                        print("No more red coins available on board\n")
                        continue
                    break
                elif(option == 4 ):
                    carrom.strikerStrike(player)
                    break
                elif( option == 5 ):
                    coin_type = input("Which coin is defuncted? red or black?\n").lower()
                    if(coin_type == "red" or coin_type == "black"):
                        if( not carrom.defunct(player,coin_type) ):
                            print("No {0} coins available".format(coin_type))
                            continue
                        break
                    else:
                        print("Coin type should be red or black\n")
                        continue
                elif( option == 6 ):
                    carrom.noneStrike(player)
                    break
            
            status,winner = checkResult(carrom)
            if( status ):
                if(winner ==  None ):
                    print("All coins exhausted !! Game Drawn !!")
                else:
                    print( "{0} won the game\n".format(winner) )

                return

            



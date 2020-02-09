#utilty functions to get various results from all objects

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

#Check result after every turn
def checkResult(carrom):

    print(getCoinStatus(carrom.coins))

    players = getAllScoresAndPlayers(carrom)

    for player in players: print("{0} : {1}".format(player.name,player.score))

    status,winner = checkWinner(players)

    if(status):
        return (status,winner)
    
    if( carrom.coins.numberOfBlackCoins == 0 and carrom.coins.numberOfRedCoins == 0 ):

        return checkWinnerIfCoinNotAvailable(players) 
    
    return (False,None)
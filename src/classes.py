class CarromCoins():

    def __new__(klaas,*args,**kwargs):

        if( not hasattr(klaas,"instance ") ):
            klaas.instance = super(CarromCoins,klaas).__new__(klaas)

        return klaas.instance

    def __init__(self,numberOfBlackCoins,numberOfRedCoins):

        self.numberOfBlackCoins = numberOfBlackCoins
        self.numberOfRedCoins = numberOfRedCoins
        self.striker = 1

class Players():

    def __init__(self,name):
        self.name = name
        self.score = 0
        self.foul = 0
        self.none_strikes = 0

class CarromGame():

    GAME_OPTIONS = [ "Strike", "Multistrike", "Red Strike", "Striker Strike", "Defunct Coin", "None" ] 

    def __new__(klass,*args,**kwargs):

        if( not hasattr(klass,"instance") ):
            klass.instance = super(CarromGame,klass).__new__(klass)
        
        return klass.instance
    
    def __init__(self,coins,players):

        self.coins = coins
        self.players = players
    

    def strike(self,player):

        if( self.coins.numberOfBlackCoins < 1 ):
            return False

        self.players[player].score+=1
        self.coins.numberOfBlackCoins-=1
        self.players[player].none_strikes = 0
        return True

    def multiStrike(self,player):
        
        if( self.coins.numberOfBlackCoins < 2 ):
            return False

        self.players[player].score+=2
        self.coins.numberOfBlackCoins-=2
        self.players[player].none_strikes = 0
        return True

    def redStrike(self,player):

        if(self.coins.numberOfRedCoins < 1 ):
            return False
        
        self.players[player].score+=3
        self.coins.numberOfRedCoins-=1
        self.players[player].none_strikes = 0
        return True
    
    def strikerStrike(self,player):
        
        self.players[player].score-=1
        self.foul(player)
        self.players[player].none_strikes = 0
        self.noneStrike(player)
        return True

    def defunct(self,player,coin_type):

        if( coin_type == "red"):

            if( self.coins.numberOfRedCoins < 1 ):
                return False
            else:
                self.coins.numberOfRedCoins-=1
                
        elif( coin_type == "black" ):

            if( self.coins.numberOfBlackCoins < 1 ):
                return False
            else:
                self.coins.numberOfBlackCoins-=1
        
        self.players[player].score-=2
        self.foul(player)
        self.noneStrike(player)
        return True

    def foul(self,player):
        self.players[player].foul+=1

        if( self.players[player].foul == 3 ):
            self.players[player].foul = 0
            self.players[player].score-=1
        
    
    def noneStrike(self,player):

        self.players[player].none_strikes+=1

        if(self.players[player].none_strikes == 3):
            self.players[player].none_strikes = 0
            self.players[player].score-=1
            self.foul(player)

    def printGameOptions(self):

        counter = 1

        for option in self.GAME_OPTIONS:
            print("{0}. {1}\n".format(counter,option) )
            counter+=1 
    
    
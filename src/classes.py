# Singleton class for creating Carraom Coins
class CarromCoins():

    def __new__(klaas,*args,**kwargs):

        if( not hasattr(klaas,"instance ") ):
            klaas.instance = super(CarromCoins,klaas).__new__(klaas)

        return klaas.instance

    def __init__(self,numberOfBlackCoins,numberOfRedCoins):

        self.numberOfBlackCoins = numberOfBlackCoins
        self.numberOfRedCoins = numberOfRedCoins
        self.striker = 1
#Class for creating players
class Players():

    def __init__(self,name):
        self.name = name
        self.score = 0
        self.foul = 0
        self.none_strikes = 0

#Singleton class for Carrom Game
class CarromGame():
    #List for all playing options
    GAME_OPTIONS = [ "Strike", "Multistrike", "Red Strike", "Striker Strike", "Defunct Coin", "None" ] 

    def __new__(klass,*args,**kwargs):

        if( not hasattr(klass,"instance") ):
            klass.instance = super(CarromGame,klass).__new__(klass)
        
        return klass.instance
    
    def __init__(self,coins,players):

        self.coins = coins
        self.players = players
    
    #Single strike black coins
    def strike(self,player):

        if( self.coins.numberOfBlackCoins < 1 ):
            return False

        self.players[player].score+=1
        self.coins.numberOfBlackCoins-=1
        self.players[player].none_strikes = 0
        return True
    #Multi strike black coins
    def multiStrike(self,player):
        
        if( self.coins.numberOfBlackCoins < 2 ):
            return False

        self.players[player].score+=2
        self.coins.numberOfBlackCoins-=2
        self.players[player].none_strikes = 0
        return True
    #Method for red coin strike
    def redStrike(self,player):

        if(self.coins.numberOfRedCoins < 1 ):
            return False
        
        self.players[player].score+=3
        self.coins.numberOfRedCoins-=1
        self.players[player].none_strikes = 0
        return True
    
    #Method for striker strike
    def strikerStrike(self,player):
        
        self.players[player].score-=1
        self.foul(player)
        self.players[player].none_strikes = 0
        self.noneStrike(player)
        return True

    #Method for defunct coins
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

        if(self.foul(player)):
            self.players[player].score-=1

        return True

    #method to keep track of all fouls
    def foul(self,player):
        
        if( self.players[player].foul == 2 ):
            self.players[player].foul = 0
            return True
        else:
            self.players[player].foul+=1
            return False
        
    #Method for no strike
    def noneStrike(self,player):

        self.players[player].none_strikes+=1

        if(self.players[player].none_strikes == 3):
            self.players[player].none_strikes = 0
            self.players[player].score-=1
            
                       
    #Methods to return all game options
    def getGameOptions(self):
        
        return CarromGame.GAME_OPTIONS

        
    
    
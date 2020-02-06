import src.utility as utility
import unittest,sys
from src.classes import CarromGame,CarromCoins,Players

class testUtility(unittest.TestCase):

    def setUp(self):
        self.coins = CarromCoins(8,1)
        self.players = [ Players("noob1"),Players("noob2") ]
        self.carrom = CarromGame(self.coins,self.players)

    def test_getAllScoresAndPlayers(self):
        scores = tuple(sorted(self.players,key=lambda x: x.score))
        self.assertEqual(scores,utility.getAllScoresAndPlayers(self.carrom))
    
    def test_printCoinStatus(self):
        coin_status = "Black Coins Left: {0}\tRed Coins Left: {1}".format(self.coins.numberOfBlackCoins,self.coins.numberOfRedCoins)
        self.assertEqual(coin_status,utility.getCoinStatus(self.coins))
    
    def test_checkWinnerFalse(self):

        self.players[0].score = 2
        self.players[1].score = 1
        players= tuple(sorted(self.players,key=lambda x: x.score))
        self.assertEqual((False,None),utility.checkWinner(players))

    def test_checkWinnerTrue(self):
    
        self.players[0].score = 5
        self.players[1].score = 1
        players= tuple(sorted(self.players,key=lambda x: x.score))
        self.assertEqual((True,players[-1].name),utility.checkWinner(players))


    def test_checkWinnerIfCoinNotAvailableGreaterThanFive(self):

        self.players[0].score = 5
        self.players[1].score = 4
        players = tuple(sorted(self.players,key=lambda x: x.score))
        self.assertEqual((True,players[-1].name),utility.checkWinnerIfCoinNotAvailable(players))
    
    def test_checkWinnerIfCoinNotAvailableDiffGreaterThanThree(self):

        self.players[0].score = 3
        self.players[1].score = 0
        players = tuple(sorted(self.players,key=lambda x: x.score))
        self.assertEqual((True,players[-1].name),utility.checkWinnerIfCoinNotAvailable(players))
    
    def test_checkWinnerIfCoinNotAvailableNoWinner(self):
    
        self.players[0].score = 3
        self.players[1].score = 2
        players = tuple(sorted(self.players,key=lambda x: x.score))
        self.assertEqual((True,None),utility.checkWinnerIfCoinNotAvailable(players))

    def test_checkResultTrueBeforeCoinExhaustion(self):
        
        self.players[0].score = 5
        self.players[1].score = 1
        self.coins.numberOfRedCoins= 1
        self.coins.numberOfBlackCoins= 2
        self.players.sort(key=lambda x: x.score)

        self.assertEqual((True,self.players[-1].name),utility.checkResult(self.carrom))
    
    def test_checkResultTrueAferCoinExhaustion(self):
        
        self.players[0].score = 3
        self.players[1].score = 0
        self.coins.numberOfRedCoins= 0
        self.coins.numberOfBlackCoins= 0
        self.players.sort(key=lambda x: x.score)

        self.assertEqual((True,self.players[-1].name),utility.checkResult(self.carrom))
    
    def test_checkResultFalseAferCoinExhaustion(self):
        
        self.players[0].score = 2
        self.players[1].score = 0
        self.coins.numberOfRedCoins= 1
        self.coins.numberOfBlackCoins= 3
        self.players.sort(key=lambda x: x.score)

        self.assertEqual((False,None),utility.checkResult(self.carrom))
    

    











if __name__ == "__main__":
    unittest.main()

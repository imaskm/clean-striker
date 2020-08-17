import unittest
from src.classes import CarromGame,CarromCoins,Players

class testCarromGame(unittest.TestCase):

    def setUp(self):
        coins = CarromCoins(8,1)
        players = [ Players("noob1"),Players("noob2") ]
        self.carromgame = CarromGame(coins,players)

    def test_ObjectCreation(self):

        self.assertIsInstance(self.carromgame,CarromGame)

    def test_strikeFalse(self):

        self.carromgame.coins.numberOfBlackCoins = 0
        self.assertEqual(False,self.carromgame.strike(player=0))
    
    def test_strikeTrue(self):

        self.carromgame.coins.numberOfBlackCoins = 1
        self.assertEqual(True,self.carromgame.strike(player=0))
    
    def test_multiStrikeFalse(self):
    
        self.carromgame.coins.numberOfBlackCoins = 1
        self.assertEqual(False,self.carromgame.multiStrike(player=0))
    
    def test_multiStrikeTrue(self):

        self.carromgame.coins.numberOfBlackCoins = 2
        self.assertEqual(True,self.carromgame.multiStrike(player=0))
    
    def test_redStrikeFalse(self):

        self.carromgame.coins.numberOfRedCoins = 0
        self.assertEqual(False,self.carromgame.redStrike(player=0))
    
    def test_redStrikeTrue(self):
        self.carromgame.coins.numberOfRedCoins = 1
        self.assertEqual(True,self.carromgame.redStrike(player=0))
    
    def test_strikerStrike(self):

        self.assertEqual(True,self.carromgame.strikerStrike(player=0))
    
    def test_defunctBlackTrue(self):
        self.carromgame.coins.numberOfBlackCoins = 1
        self.assertEqual(True,self.carromgame.defunct(player=0,coin_type='black'))
    
    def test_defunctBlackFalse(self):
        self.carromgame.coins.numberOfBlackCoins = 0
        self.assertEqual(False,self.carromgame.defunct(player=0,coin_type='black'))
    
    def test_defunctRedTrue(self):
        self.carromgame.coins.numberOfRedCoins = 1
        self.assertEqual(True,self.carromgame.defunct(player=0,coin_type='red'))
    
    def test_defunctTrueFourTrue(self):
        self.carromgame.coins.numberOfRedCoins = 1
        player = 0
        self.carromgame.players[player].foul = 2
        self.assertEqual(True,self.carromgame.defunct(player=player,coin_type='red'))
    
    def test_defunctRedFalse(self):
        self.carromgame.coins.numberOfRedCoins = 0
        self.assertEqual(False,self.carromgame.defunct(player=0,coin_type='red'))
    
    def test_foulTrue(self):
        player = 0
        self.carromgame.players[player].foul = 2
        print((self.carromgame.players[player].foul))
        self.assertEqual(True,self.carromgame.foul( player=0 ))
    
    def test_foulFalse(self):
        player = 0
        self.carromgame.players[player].foul = 1
        print((self.carromgame.players[player].foul))
        self.assertEqual(False,self.carromgame.foul( player=0 ))
    
    def test_noneStrikeNotThree(self):
        player = 0
        none_strikes = self.carromgame.players[player].none_strikes
        self.carromgame.noneStrike(player)
        self.assertEqual(none_strikes+1,self.carromgame.players[player].none_strikes)
    
    def test_noneStrikeThree(self):
        player = 0
        self.carromgame.players[player].none_strikes = 2
        self.carromgame.players[player].score = 5
        self.carromgame.noneStrike(player)
        self.assertEqual([0,4], [self.carromgame.players[player].none_strikes,self.carromgame.players[player].score])
    
    def test_gameOptions(self):

        self.assertEqual(self.carromgame.GAME_OPTIONS,self.carromgame.getGameOptions()) 

    def test_superFoul(self):

        expected_scores=[]
        player = 0

        for i in range(len(self.carromgame.players)):
            if(i==player):
                expected_scores.append(self.carromgame.players[i].score-2)
            else:
                expected_scores.append(self.carromgame.players[i].score+1)
        self.carromgame.superFoul(player)

        scores=[]

        for player in self.carromgame.players:
            scores.append(player.score)

        self.assertEqual(expected_scores,scores)


#to run test without unittest option on cli
'''if __name__ == "__main__":
    unittest.main()'''
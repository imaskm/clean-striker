
import unittest
from src.classes import CarromGame,CarromCoins,Players

class testPlayer(unittest.TestCase):

    def setUp(self):
        self.coins = CarromCoins(8,1)
        
        self.players = [ Players("noob1"),Players("noob2") ]

    def test_object_creation(self):
        
        obj_player=CarromGame(self.coins,self.players)
        self.assertIsInstance(obj_player,CarromGame)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.classes import CarromCoins

class testPlayer(unittest.TestCase):

    def test_object_creation(self):
        blackCoins = 9
        redCoins = 1
        obj_player=CarromCoins(blackCoins,redCoins)
        self.assertIsInstance(obj_player,CarromCoins)


if __name__ == "__main__":
    unittest.main()
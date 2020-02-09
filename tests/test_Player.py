import unittest
from src.classes import Players

class testPlayer(unittest.TestCase):

    def test_object_creation(self):
        name = "test"
        obj_player=Players(name)
        self.assertIsInstance(obj_player,Players)
#to run test without unittest option on cli
'''if __name__ == "__main__":
    unittest.main()'''

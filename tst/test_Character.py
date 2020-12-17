#!/usr/bin/python
import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Character import Character

class CharacterTest(unittest.TestCase):


    def setUp(self):
        pass


    def test_character_existance(self):
        character = Character()
        self.assertIsInstance(character,Character,'Not a Match')
        # self.assertIsInstance(character, str,'Not a Match')


if __name__ == '__main__':
    unittest.main()

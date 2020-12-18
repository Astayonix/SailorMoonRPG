#!/usr/bin/python
import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Hero import Hero

class HeroTest(unittest.TestCase):


    def setUp(self):
        pass


    def test_hero_existance(self):
        hero = Hero()
        self.assertIsInstance(hero,Hero,'Not a Match')


if __name__ == '__main__':
    unittest.main()

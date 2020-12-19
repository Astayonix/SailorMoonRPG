#!/usr/bin/python
import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Hero import Hero

class HeroTest(unittest.TestCase):


    def setUp(self):
        self.hero = Hero('Serena')
        self.hero2 = Hero('Elena')


    def test_hero_existance(self):
        self.assertIsInstance(self.hero,Hero,'Not a Match')


    def test_hero_name_setter(self):
        self.assertIs(self.hero.name, 'Serena', 'Not a Match')


    def multi_player_test(self):
        print(self.hero)
        print(self.hero2)
        self.assertEquals(self.hero, self.hero2, 'Not a Match')


    def tearDown(self):
        del self.hero
        del self.hero2


if __name__ == '__main__':
    unittest.main()

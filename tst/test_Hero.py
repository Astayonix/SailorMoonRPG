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
        self.assertIsInstance(self.hero,Hero,'Not a Hero')


    def test_hero_name_setter(self):
        self.assertIs(self.hero.name, 'Serena', 'No Name Detected')


    def test_multi_player(self):
        self.assertNotEqual(self.hero, self.hero2, '{} =! {}'.format(self.hero, self.hero2))


    def tearDown(self):
        del self.hero
        del self.hero2


if __name__ == '__main__':
    unittest.main()

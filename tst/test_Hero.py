#!/usr/bin/python
import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Hero import Hero

class HeroTest(unittest.TestCase):


    def setUp(self):
        hero = Hero('Akum Ra')


    def test_hero_existance(self):
        hero = Hero()
        self.assertIsInstance(hero,Hero,'Not a Match')

    def test_hero_name_setter(self):
        self.assertIs(hero.name, 'Akum Ra', 'Not a Match')


if __name__ == '__main__':
    unittest.main()

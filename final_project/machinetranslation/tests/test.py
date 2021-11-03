""" This module is used to test the translator module"""

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrance(unittest.TestCase):
    """ This class wil test the english_to_french metohd """
    def test1(self):
        """ The test includes 3 test case"""
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Yes'),'Oui')
        self.assertNotEqual(english_to_french('Hello'),'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    """ This class wil test the french_to_english metohd """
    def test2(self):
        """ The test includes 3 test case"""
        self.assertEqual(french_to_english(' '),' ')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Oui'),'Yes')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')

unittest.main()

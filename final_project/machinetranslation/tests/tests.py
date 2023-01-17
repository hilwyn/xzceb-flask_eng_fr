import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        input_text = 'Bonjour'
        expected_output_text = 'Hello'
        self.assertEqual(french_to_english(input_text), expected_output_text) # translate bonjou to hello
        self.assertIs(french_to_english(None), True) #Function should return None when input is None

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        input_text = 'Hello'
        expected_output_text = 'Bonjour'
        self.assertEqual(english_to_french(input_text), expected_output_text) # translate hello to bonjou
        self.assertIs(english_to_french(None), True) #Function should return None when input is None

unittest.main()
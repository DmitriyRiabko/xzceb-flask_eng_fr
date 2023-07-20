import unittest

import translator 

class TestStringMethods(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english("Bonjour"),"Hello")

    def test_french_to_not_english(self):
        self.assertNotEqual(translator.french_to_english("Bonjour"),"Bonjour")


    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french("Hello"),"Bonjour")
    

    def test_english_to_not_french(self):
        self.assertNotEqual(translator.english_to_french("Hello"),"Hello")
    

    
if __name__ == '__main__':
    unittest.main()

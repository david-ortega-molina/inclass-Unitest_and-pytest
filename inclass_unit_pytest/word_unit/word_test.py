import unittest
import wordcounter

class testPalindrom(unittest.TestCase):
    def test1(self):
        self.assertEqual(wordcounter.word_counter('this is four words' ), 4)
    
    def test2(self):
        self.assertEqual(wordcounter.word_counter('this is more than four words' ), 6)
    
    def test3(self):
        self.assertEqual(wordcounter.word_counter('this is five words' ), 5)

    
    



if __name__ == '__main__':
    unittest.main()
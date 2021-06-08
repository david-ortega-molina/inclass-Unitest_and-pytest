import unittest
import pal

class testPalindrom(unittest.TestCase):
    def test1(self):
        self.assertEqual(pal.palindrome_checker('hannah' ), 'hannah')

    def test2(self):
        self.assertEqual(pal.palindrome_checker('david'), 'david')
    
    



if __name__ == '__main__':
    unittest.main()
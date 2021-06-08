import pal

def test_pal():
    assert 'hannah' == pal.palindrome_checker('hannah')

def test_pal2():
    assert 'car' == pal.palindrome_checker('car')

def test_pal3():
    assert 'racecar' == pal.palindrome_checker('racecar')
import wordcounter

def test1():
    assert 4 == wordcounter.word_counter('this is four words')

def test2():
    assert 5 == wordcounter.word_counter('this is five words')
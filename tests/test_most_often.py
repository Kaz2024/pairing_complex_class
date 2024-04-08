from lib.most_often import *

def test_initialisation():
    mostoften = MostOften([1, 2])
    assert mostoften.starting_list == [1,2]

def test_add_new():
    mostoften = MostOften([1, 2])
    mostoften.add_new(3)
    assert mostoften.starting_list == [1, 2, 3]

def test_highest_count():
    mostoften = MostOften([1, 1, 2])
    assert mostoften.get_most_often() == 1

def test_no_winner():
    mostoften = MostOften([1, 1, 2, 2])
    assert mostoften.get_most_often() == "no clear winner"
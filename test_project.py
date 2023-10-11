from project import get_lives, nonzero_lives, all_correct


def test_get_lives():
    assert get_lives(1) == -1
    assert get_lives(2) == 10
    assert get_lives(3) == 1


def test_nonzero_lives():
    assert nonzero_lives(10) == True
    assert nonzero_lives(1) == True
    assert nonzero_lives(-1) == True
    assert nonzero_lives(0) == False


def test_all_correct():
    assert all_correct(46, 46) == True
    assert all_correct(45, 46) == False
    assert all_correct(1, 1) == True
    assert all_correct(0, 10) == False

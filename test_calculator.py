from calculator import divide, multiply


def test_divide():
    assert divide(10, 2) == 5


def test_multiply():
    assert multiply(3, 4) == 12

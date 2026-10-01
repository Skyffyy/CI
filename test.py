from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero():
    try:
        divide(5, 0)
        assert False
    except ValueError:
        pass


test_add()
test_subtract()
test_multiply()
test_divide()
test_divide_by_zero()

print("All tests passed!")
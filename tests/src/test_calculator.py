from app.src.calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1, 3) == 4
    assert cal.add(1, 1) == 2

def test_subtract():
    assert cal.subtract(3, 2) == 1
    assert cal.subtract(3, 1) == 2

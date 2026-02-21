import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_divide_error():
    # This test will intentionally trigger the bug
    assert calculator.divide(10, 0) == 0

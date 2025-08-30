from calculator import add, substract

def test_add():
    assert add(2,3) == 5

def test_substract():
    assert substract(5,3) == 2

# adding a failing test
# def test_failing_example():
#     assert add(2,2) == 5
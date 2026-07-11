from myapp import add, substract

# this method can add two numbers
def test_add ():
    assert add(3,4) == 7

# this method can substract numbers
def test_subtract ():
    assert substract(3,4) == -1
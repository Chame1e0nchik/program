from myapp.app import add, subtract

# this method can add two numbers
def test_add ():
    assert add(3,4) == 7

# this method can subtract numbers
def test_subtract ():
    assert subtract(3,4) == -1
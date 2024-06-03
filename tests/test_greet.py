from lib.greet import *

def test_greet_returns_this():
    name = greet("Dora")
    result = "Hello, Dora!"
    assert result == "Hello, Dora!"
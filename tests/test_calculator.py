import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator import add, subtract, multiply, divide

#addition test cases
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

#subtration test cases
def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(1, 2) == -1

#multiptication test cases
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 2) == -2

#division test cases
def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(1, 0) == "Error: Division by zero."

import pytest
import random
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("x, y", [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)])
def test_add(x, y):
    result = add(x, y)
    print(f"Adding {x} and {y}: Result = {result}")
    assert result == x + y

@pytest.mark.parametrize("x, y", [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)])
def test_subtract(x, y):
    result = subtract(x, y)
    print(f"Subtracting {y} from {x}: Result = {result}")
    assert result == x - y

@pytest.mark.parametrize("x, y", [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)])
def test_multiply(x, y):
    result = multiply(x, y)
    print(f"Multiplying {x} by {y}: Result = {result}")
    assert result == x * y

@pytest.mark.parametrize("x, y", [(random.randint(1, 100), random.randint(1, 100)) for _ in range(10)])
def test_divide(x, y):
    result = divide(x, y)
    print(f"Dividing {x} by {y}: Result = {result}")
    assert result == pytest.approx(x / y)
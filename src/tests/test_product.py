import pytest
from products import Product

def test_is_in_stock():
    prod1, prod2 = Product("test", 1.0, 0), Product("test", 1.0, 4)
    s1, s2 = prod1.is_in_stock(), prod2.is_in_stock()
    assert s1 == False
    assert s2 == True 

def test_stock_setter_negative():
    with pytest.raises(ValueError, match = "Stock should be >= 0"):
        prod1 = Product("test", 1.0, -2)

def test_stock_setter_string():
    with pytest.raises(ValueError, match = "Stock should be an integer"):
        prod1 = Product("test", 1.0, "test")




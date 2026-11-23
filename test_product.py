from product import product

def test_product():
    result = product(101, "Laptop", 5, 50000)

    expected = "Product ID: 101, Name: Laptop, Quantity: 5, Price: 50000"

    assert result == expected
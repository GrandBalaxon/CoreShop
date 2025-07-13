import pytest

from src.classes import Product


@pytest.fixture()
def a_test_product():
    product = Product("test product", "description", 100.0, 5)

    return product

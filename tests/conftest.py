import pytest

from src.product import Product


@pytest.fixture()
def a_test_product():
    product = Product("test product", "description", 100.0, 5)

    return product


@pytest.fixture()
def json_file_output():
    return [
  {
    "name": "Category #1",
    "description": "Category description #1",
    "products": [
      {
        "name": "UNO",
        "description": "Product description #1",
        "price": 100.0,
        "quantity": 1
      },
      {
        "name": "DOS",
        "description": "Product description #2",
        "price": 200.0,
        "quantity": 2
      }
    ]
  },
  {
    "name": "Category #2",
    "description": "Category description #2",
    "products": [
      {
        "name": "UNO",
        "description": "Product description #3",
        "price": 300.0,
        "quantity": 3
      }
    ]
  }
]

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone


@pytest.fixture()
def a_test_product():
    product = Product("test product", "description", 100.0, 5)

    return product


@pytest.fixture()
def a_test_smartphone():
    smartphone = Smartphone(
        "Nothing Phone 2(a)",
        "Cool description",
        52000.0,
        5,
        52.5,
        "Phone 2(a)",
        256,
        "White"
    )
    return smartphone


@pytest.fixture()
def a_test_grass():
    grass = LawnGrass(
        "A test grass",
        "Cool description",
        52000.0,
        1000,
        "Canada",
        "28 days",
        "Gorgeous"
    )
    return grass


@pytest.fixture()
def category_obj(a_test_product):
    cat = Category(
        "category name",
        "category description",
        [a_test_product, a_test_product, a_test_product]
    )
    return cat


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

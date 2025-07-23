import pytest

from src.product import Product


def test_product_class_object_creation():
    """ Проверка правильной инициализации объекта класса Product. """
    product = Product("Some thing", "test description", 52.0, 7)

    assert product.name == "Some thing"
    assert product.description == "test description"
    assert product.price == 52.0
    assert product.quantity == 7


def test_adding_new_product_with_a_same_name():
    """ Проверка правильной работы метода класса .new_product при добавлении товара с тем же именем. """
    product = Product("Product #1", "Description #1", 100.0, 1)

    assert product.price == 100.0
    assert product.quantity == 1

    new_product = Product.new_product({
        "name": "Product #1",
        "description": "Description #1",
        "price": 200.0,
        "quantity": 2
    })

    assert product.price == 200.0
    assert product.quantity == 3
    assert new_product.price == 200.0
    assert new_product.quantity == 3
    assert product == new_product

    new_product_2 = Product.new_product({
        "name": "Product #2",
        "description": "Description #2",
        "price": 300.0,
        "quantity": 5
    })

    assert new_product_2.price == 300.0
    assert new_product_2.quantity == 5


def test_adding_new_price_to_a_product(a_test_product):
    """ Проверка правильной работы назначения новой цены выше текущей. """
    product = a_test_product
    assert product.price == 100.0

    product.price = 200.0
    assert product.price == 200.0


def test_adding_new_negative_price(a_test_product, capsys):
    """ Проверка правильной работы назначения новой цены равной нулю. """
    product = a_test_product
    product.price = -100.0
    captured = capsys.readouterr()

    assert product.price == 100.0
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_adding_new_price_lower_than_current(a_test_product, mocker, capsys):
    """ Проверка корректной работы при добавлении цены ниже текущей. """
    product = a_test_product
    product.price = 1000.0
    assert product.price == 1000.0

    # Тестируем наше не согласие на изменение
    mocker.patch("builtins.input", return_value="N")
    product.price = 500.0
    captured = capsys.readouterr()

    assert product.price == 1000.0
    assert ("Новая цена 500.0 ниже предыдущей 1000.0.\n"
            "Цена товара test product осталась прежней: 1000.0\n") in captured.out

    # Тестируем наше согласие на изменение
    mocker.patch("builtins.input", return_value="Y")
    product.price = 500.0

    assert product.price == 500.0


def test_adding_two_products(a_test_product):
    """ Тестируем сложение двух товаров. """
    result = a_test_product + a_test_product

    assert result == 1000.0


def test_type_error_while_adding_up_product_and_non_product(a_test_product):
    """ Тестируем возбуждение ошибки при сложении товара и НЕ товара. """
    with pytest.raises(TypeError):
        result = a_test_product + 2

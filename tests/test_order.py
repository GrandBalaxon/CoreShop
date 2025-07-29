import pytest

from src.order import Order


def test_order_successful_creation(a_test_smartphone):
    """ Тест успешного создания экземпляра класса Order. """
    order = Order(a_test_smartphone, 5)

    assert order.product == "Nothing Phone 2(a)"
    assert order.quantity == 5
    assert order.total_price == 52000.0 * 5


def test_order_product_addition_failure(a_test_smartphone):
    """ Тест неудачной попытки добавить товар в заказ. """
    order = Order(a_test_smartphone, 5)

    with pytest.raises(Exception, match="Заказ может содержать только один товар."):
        order.add_product(a_test_smartphone)


def test_adding_a_non_product_obj_to_an_order(capsys):
    """ Тест поведения при добавлении объекта не класса Product или дочерних в заказ. """
    order = Order("Not a Product", 5)
    captured = capsys.readouterr()

    assert "Несовместимый тип товара." in captured.out


def test_str_method(a_test_smartphone):
    """ Проверяем вывод через функцию str(). """
    order = Order(a_test_smartphone, 5)
    assert str(order) == "Заказ: Nothing Phone 2(a), 5 шт. Итого: 260000.0 руб."

import pytest

from src.iterator import CategoryIterator


def test_category_iterator_normal_functioning(category_obj, a_test_product):
    """ Проверка нормальной работы класса итератора. """
    iter_ = iter(CategoryIterator(category_obj))

    assert next(iter_) == a_test_product
    assert next(iter_) == a_test_product
    assert next(iter_) == a_test_product

    with pytest.raises(StopIteration):
        assert next(iter_) == a_test_product


def test_type_error(a_test_product):
    """ Тестируем поднятие ошибки TypeError. """
    with pytest.raises(TypeError, match="Неверный тип данных."):
        iter(CategoryIterator(a_test_product))

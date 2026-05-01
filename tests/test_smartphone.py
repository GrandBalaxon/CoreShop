import pytest


def test_smartphone_class_object_creation(a_test_smartphone):
    """ Проверка правильной инициализации объекта класса Product. """
    ph1 = a_test_smartphone

    assert ph1.name == "Nothing Phone 2(a)"
    assert ph1.description == "Cool description"
    assert ph1.price == 52000.0
    assert ph1.quantity == 5
    assert ph1.efficiency == 52.5
    assert ph1.model == "Phone 2(a)"
    assert ph1.memory == 256
    assert ph1.color == "White"


def test_smartphones_addition(a_test_smartphone):
    """ Проверка правильного сложения двух позиций смартфонов. """
    result1 = a_test_smartphone + a_test_smartphone
    assert result1 == 52000.0 * 10

    # Проверяем выбрасывание ошибки при попытке сложения с объектом другого класса
    with pytest.raises(TypeError):
        result2 = a_test_smartphone + 100.0

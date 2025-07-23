import pytest


def test_lawn_grass_class_object_creation(a_test_grass):
    """ Проверка правильной инициализации объекта класса Product. """
    grass = a_test_grass

    assert grass.name == "A test grass"
    assert grass.description == "Cool description"
    assert grass.price == 52000.0
    assert grass.quantity == 1000
    assert grass.country == "Canada"
    assert grass.germination_period == "28 days"
    assert grass.color == "Gorgeous"


def test_smartphones_addition(a_test_grass):
    """ Проверка правильного сложения двух позиций смартфонов. """
    result1 = a_test_grass + a_test_grass
    assert result1 == 52000.0 * 1000 * 2

    # Проверяем выбрасывание ошибки при попытке сложения с объектом другого класса
    with pytest.raises(TypeError):
        result2 = a_test_grass + 100.0

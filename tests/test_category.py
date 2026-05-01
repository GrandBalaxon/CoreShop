import pytest

from src.category import Category
from src.product import Product


def test_category_class_object_creation(a_test_product):
    """ проверка правильной инициализации нескольких объектов класса Category. """
    # Обнуляем атрибуты класса для теста
    Category.category_count = 0
    Category.product_count = 0

    category_1 = Category("Category name UNO",
                        "test description #1",
                        [a_test_product, a_test_product])

    assert category_1.name == "Category name UNO"
    assert category_1.description == "test description #1"
    assert len(category_1.products_list) == 2

    # Проверка значений атрибутов класса до ввода второй категории
    assert Category.category_count == 1
    assert Category.product_count == 2

    category_2 = Category("Category name DOS",
                          "test description #2",
                          [a_test_product])

    assert category_2.name == "Category name DOS"
    assert category_2.description == "test description #2"
    assert len(category_2.products_list) == 1

    # Проверка значений атрибутов класса после ввода второй категории
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_add_product_method(a_test_product):
    """ Тестируем работу метода add_product. """
    Category.category_count = 0
    Category.product_count = 0
    category_1 = Category("Category name UNO",
                          "test description #1",
                          [a_test_product, a_test_product])

    assert len(category_1.products_list) == 2
    assert Category.product_count == 2

    category_1.add_product(a_test_product)

    assert len(category_1.products_list) == 3
    assert Category.product_count == 3


def test_failed_attempt_to_add_not_a_product(a_test_product, capsys):
    """ Проверка на добавления объекта класса НЕ Product в объект Category через метод .add_product """
    class TestClass:
        def __init__(self, test_param: int):
            self.test_param = test_param

    Category.category_count = 0
    Category.product_count = 0
    category_1 = Category("Category name UNO",
                          "test description #1",
                          [a_test_product, a_test_product])

    assert len(category_1.products_list) == 2
    assert Category.product_count == 2

    non_product = TestClass(6)
    category_1.add_product(non_product)
    captured = capsys.readouterr()

    assert "Несовместимый тип товара" in captured.out
    assert len(category_1.products_list) == 2
    assert Category.product_count == 2


def test_products_info_str(a_test_product):
    """ Тестирование работы геттера .products_info_str """
    category_1 = Category("Category name UNO",
                          "test description #1",
                          [a_test_product, a_test_product])

    result = category_1.products
    expected_str = "test product, 100.0 руб. Остаток: 5 шт.\ntest product, 100.0 руб. Остаток: 5 шт."

    assert result == expected_str


def test_products_info_str_empty():
    """ Тестируем работу геттера с категорией с пустым списком товаров. """
    category_1 = Category("Category name UNO",
                          "test description #1",
                          [])

    result = category_1.products
    assert result == ""


def test_category_obj_str_representation(category_obj):
    """ Проверка правильной работы переопределенного метода __str__.  """
    assert str(category_obj) == "category name, количество продуктов: 15 шт."


def test_type_error_with_different_products_classes(a_test_product, a_test_smartphone):
    """ Проверка возбуждения ошибки при попытке создать категорию товаров, добавляя товары разных классов. """
    with pytest.raises(TypeError, match="В категории товары должны иметь одинаковый класс."):
        category_1 = Category("Category name UNO",
                              "test description #1",
                              [a_test_smartphone, a_test_product])


def test_zero_quantity_error(capsys):
    """ Тестирование работы при добавлении товара с 0 единиц на складе в категорию. """
    category_1 = Category("Cat Name", "test desc", [])

    pr = Product("test name", "test description", 100.0, 1)
    pr.quantity -= 1
    category_1.add_product(pr)
    captured = capsys.readouterr()

    assert "Товар с нулевым количеством не может быть добавлен." in captured.out


def test_same_class_requirement_for_category(category_obj, a_test_smartphone, capsys):
    """Проверяем добавление товара иного класса в категорию."""
    category_1 = category_obj
    category_1.add_product(a_test_smartphone)
    captured = capsys.readouterr()

    assert a_test_smartphone.__class__ != category_1.category_class
    assert "В категории товары должны иметь одинаковый класс." in captured.out


def test_middle_price(category_obj, a_test_product):
    """Тестируем работу метода определения средней цены товаров в категории."""
    cat1 = category_obj
    assert cat1.middle_price() == a_test_product.price

    cat2 = Category("Name", "Disc", [])
    assert cat2.middle_price() == 0

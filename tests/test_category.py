from src.category import Category


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

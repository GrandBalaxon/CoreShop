from src.category import Category


class CategoryIterator:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории.

    Attributes:
        current_product_index: Текущий индекс товара в категории
        stop_point: Индекс остановки итерации
    """

    def __init__(self, category: Category):
        if isinstance(category, Category):
            self.products_list = category.products_list
            self.current_product_index = -1
        else:
            raise TypeError("Неверный тип данных.")

    def __iter__(self):
        """Возвращает итератор."""
        self.current_product_index = -1
        self.stop_point = len(self.products_list) - 1
        return self

    def __next__(self):
        """Возвращает следующий товар в категории."""
        if self.current_product_index < self.stop_point:
            self.current_product_index += 1
            return self.products_list[self.current_product_index]
        else:
            raise StopIteration

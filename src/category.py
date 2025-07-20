from typing import List

from src.product import Product


class Category:
    """Класс для представления категории товаров в магазине

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        __products (List[Product]): Список продуктов
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_count = 0
        for pr in self.__products:
            total_count += pr.quantity

        return f"{self.name}, количество продуктов: {total_count} шт."

    def add_product(self, product_to_add: Product):
        """ Добавляет продукт в категорию. """
        if isinstance(product_to_add, Product):
            self.__products.append(product_to_add)

            Category.category_count += 1
            Category.product_count += 1

    @property
    def products_list(self):
        """ Геттер для получения списка товаров в виде списка. """
        return self.__products

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в виде строки.

        :return: Строка, содержащая список товаров в формате: "Название продукта, 80 руб. Остаток: 15 шт."
        Каждый новый товар отображается на новой строке.
        Если список товаров пуст, возвращает пустую строку.
        """
        if not self.__products:
            return ""

        output_str = ""
        for pr in self.__products:
            output_str += f"{str(pr)}\n"

        return output_str.strip()

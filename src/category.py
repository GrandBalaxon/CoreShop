from typing import List

from src.product import Product


class Category:
    """Класс для представления категории товаров в магазине

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        products (List[Product]): Список продуктов
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(self.products)

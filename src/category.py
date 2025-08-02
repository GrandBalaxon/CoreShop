from typing import List, Union

from src.base_abs import ProductContainer, ProductType
from src.exceptions import ZeroQuantityError
from src.product import Product


class Category(ProductContainer):
    """Класс для представления категории товаров в магазине

    Attributes:
        name (str): Название категории
        description (str): Описание категории
        __products (List[Product]): Список продуктов
        __category_class: Класс товаров в категории (одинаков для каждого товара категории)
        category_count: Счетчик одновременно существующих разных категорий товаров
        product_count: Счетчик видов товаров во всех категориях
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[ProductType]) -> None:
        self.name = name
        self.description = description

        # Проверяем, что продукты категории имеют один и тот же класс
        if len(products) >= 1:
            self.__category_class = products[0].__class__
            if len(products) > 1:
                for pr in products[1:]:
                    if pr.__class__ is not self.__category_class:
                        raise TypeError("В категории товары должны иметь одинаковый класс.")
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        total_count = 0
        for pr in self.__products:
            total_count += pr.quantity

        return f"{self.name}, количество продуктов: {total_count} шт."

    def add_product(self, product_to_add: ProductType) -> None:
        """Добавляет продукт в категорию."""
        try:
            if not isinstance(product_to_add, Product):
                raise TypeError("Несовместимый тип товара.")
            else:
                # проверка на соответствие класса категории
                try:
                    if type(product_to_add) is not self.__category_class:
                        raise TypeError("В категории товары должны иметь одинаковый класс.")
                except AttributeError:
                    pass

            if product_to_add.quantity == 0:
                raise ZeroQuantityError()

            self.__products.append(product_to_add)
            Category.product_count += 1
            print("Товар успешно добавлен.")

        except (TypeError, ZeroQuantityError) as e:
            print(str(e))
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def category_class(self) -> type[ProductType]:
        """Геттер для отладочного получения класса категории."""
        return self.__category_class

    @property
    def products_list(self) -> List[ProductType]:
        """Геттер для получения списка товаров в виде списка."""
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

    def middle_price(self) -> Union[float, int]:
        """
        Метод для расчёта среднего ценника всех товаров в категории.
        При пустом списке товаров вернет 0.
        """
        try:
            mid_price = sum([x.price for x in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return round(mid_price, 2)

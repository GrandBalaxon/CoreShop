from src.base_abs import ProductContainer, ProductType
from src.product import Product


class Order(ProductContainer):
    """Класс для представления заказа в магазине

    Attributes:
        __product: Товар класса Product или его подклассов
        __quantity: Количество единиц купленного товара
        __total_price: Стоимость заказа
    """

    def __init__(self, product: ProductType, quantity: int):
        if isinstance(product, Product):
            self.__product = product.name
            self.__quantity = quantity
            self.__total_price = self.__quantity * product.price
        else:
            raise TypeError

    def __str__(self):
        return f"Заказ: {self.__product}, {self.__quantity} шт. Итого: {self.__total_price} руб."

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def total_price(self):
        return self.__total_price

    def add_product(self, product_to_add: ProductType):
        raise Exception("Заказ может содержать только один товар.")

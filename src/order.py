from src.base_abs import ProductContainer, ProductType
from src.product import Product
from src.exceptions import ZeroQuantityError


class Order(ProductContainer):
    """Класс для представления заказа в магазине

    Attributes:
        __product: Товар класса Product или его подклассов
        __quantity: Количество единиц купленного товара
        __total_price: Стоимость заказа
    """

    def __init__(self, product: ProductType, quantity: int) -> None:
        try:
            if not isinstance(product, Product):
                raise TypeError("Несовместимый тип товара.")

            if quantity == 0:
                raise ZeroQuantityError("Запрещено создавать заказ на ноль единиц купленного товара.")
            if product.quantity == 0:
                raise ZeroQuantityError()

            self.__product = product.name
            self.__quantity = quantity
            self.__total_price = self.__quantity * product.price
            print("Товар успешно добавлен в заказ.")

        except (TypeError, ZeroQuantityError) as e:
            print(str(e))
        finally:
            print("Обработка заказа завершена.")

    def __str__(self) -> str:
        return f"Заказ: {self.__product}, {self.__quantity} шт. Итого: {self.__total_price} руб."

    @property
    def product(self) -> str:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def total_price(self) -> float:
        return self.__total_price

    def add_product(self, product_to_add: ProductType) -> None:
        raise Exception("Заказ может содержать только один товар.")

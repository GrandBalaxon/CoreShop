from typing import Any, Dict, List


class Product:
    """Класс для представления товара в магазине

    Attributes:
        name (str): Название товара
        description (str): Описание товара
        __price (float): Цена товара
        quantity (int): Количество товара на складе
    """

    __products_list: List["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.__products_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product"):
        if type(other) is Product:
            total_products_price = self.__price * self.quantity + other.__price * other.quantity
            return total_products_price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]):
        """
        Создает новый объект Product на основе словаря данных.

        :param product_data: Словарь с данными о новом продукте.
        Должен обязательно содержать ключи: name, description, price, quantity.

        :return: Новый или обновленный объект Product.
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        for product in cls.__products_list:
            if product.name == name:
                # Обновляем цену, если у нового товара она выше
                if price > product.price:
                    product.price = price
                # Обновляем количество товаров на складе
                product.quantity += quantity

                return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для получения цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для установки новой цены товара.

        :param new_price: Новая цена. Должна быть больше нуля, иначе выводится сообщение об ошибке.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            print(f"Новая цена {float(new_price)} ниже предыдущей {self.__price}.")
            user_input = input("Подтвердите операцию (Y/N): ")

            if user_input.lower() == "y":
                self.__price = float(new_price)
            else:
                print(f"Цена товара {self.name} осталась прежней: {self.__price}")

        else:
            self.__price = float(new_price)

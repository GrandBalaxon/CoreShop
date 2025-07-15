from typing import Any, Dict


class Product:
    """Класс для представления товара в магазине

    Attributes:
        name (str): Название товара
        description (str): Описание товара
        price (float): Цена товара
        quantity (int): Количество товара на складе
    """

    __products_list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.__products_list.append(self)

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]):
        """ Создает новый объект Product на основе словаря данных. """
        new_product = cls(
            name=product_data["name"],
            description = product_data["description"],
            price = product_data["price"],
            quantity = product_data["quantity"]
        )

        for pr in cls.__products_list:
            if pr.name == new_product.name:
                # Обновляем цену, если у нового товара она выше
                if new_product.price > pr.price:
                    pr.price = new_product.price

                # Обновляем количество товаров на складе
                pr.quantity += new_product.quantity

                return pr

        return new_product

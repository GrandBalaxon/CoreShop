from src.product import Product


class Smartphone(Product):
    """Отдельный класс для товаров категории смартфоны.

    Attributes:
        efficiency: Производительность
        model: Модель
        memory: Объём встроенной памяти
        color: Цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone"):
        """Сложение с продуктами одинаковой категории."""
        if type(other) is Smartphone:
            total_products_price = self.price * self.quantity + other.price * other.quantity
            return total_products_price
        else:
            raise TypeError

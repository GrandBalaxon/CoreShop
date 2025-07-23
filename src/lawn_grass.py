from src.product import Product


class LawnGrass(Product):
    """Отдельный класс для товаров категории трава газонная.

    Attributes:
        country: Страна-производитель
        germination_period: Срок прорастания
        color: Цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass"):
        """Сложение с продуктами одинаковой категории."""
        if type(other) is LawnGrass:
            total_products_price = self.price * self.quantity + other.price * other.quantity
            return total_products_price
        else:
            raise TypeError

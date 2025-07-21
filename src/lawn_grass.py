from src.product import Product


class LawnGrass(Product):
    """ Отдельный класс для товаров категории трава газонная.  """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

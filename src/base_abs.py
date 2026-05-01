from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from src.product import Product

ProductType = TypeVar("ProductType", bound="Product")


class BaseProduct(ABC):
    """Абстрактный базовый класс для товара."""

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class ProductContainer(ABC):
    """Абстрактный базовый класс для контейнеров с продуктами любого типа."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_product(self, product_to_add: ProductType):
        pass

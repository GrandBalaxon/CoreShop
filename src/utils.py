import json
import logging
from pathlib import Path
from typing import List, Optional

from src.classes import Category, Product

logger = logging.getLogger("utils")


def get_categories_objects_from_json(file_name: str) -> Optional[List[Category]]:
    """
    Функция для извлечения списка словарей категорий продуктов из JSON-файла.

    :param file_name: Имя JSON-файла расположенного в папке data/
    :return: Список объектов класса Category, содержащих объекты класса Products
    """
    try:
        file_path = Path(__file__).parent.parent / "data" / file_name

        try:
            with open(file_path, encoding="UTF-8") as file:
                list_ = json.load(file)
                logger.info(f"Успешно изъято {len(list_)} словаря-категории из файла {file_name}")
        except FileNotFoundError:
            logger.error(f"Нет такого файла: {file_name}")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка парсинга файла {file_name}: {str(e)}")
            return None

        categories_list = []

        for category in list_:
            products_list = []

            for prod in category["products"]:
                product_ = Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
                products_list.append(product_)

            category_ = Category(category["name"], category["description"], products_list)
            categories_list.append(category_)

        logger.info("Список категорий успешно обработан")
        return categories_list

    except Exception as e:
        logger.error(f"непредвиденная ошибка: {str(e)}")
        return None


if __name__ == "__main__":
    _name = "products.json"
    ew = get_categories_objects_from_json(_name)
    print(ew)

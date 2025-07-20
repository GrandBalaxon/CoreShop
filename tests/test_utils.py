import json
from unittest.mock import mock_open

from src.category import Category
from src.utils import get_categories_objects_from_json


def test_data_successful_load(mocker, json_file_output):
    """ Проверка успешной загрузки JSON-файла и перевода содержимого в правильные классы. """
    file_name = "test.json"

    # Обнуляем атрибуты класса для теста
    Category.category_count = 0
    Category.product_count = 0

    mocker.patch("builtins.open", mock_open(read_data=json.dumps(json_file_output)))
    mocker.patch("json.load", return_value=json_file_output)

    result = get_categories_objects_from_json(file_name)
    category_1 = result[0]
    category_2 = result[1]

    assert category_1.name == "Category #1"
    assert category_1.description == "Category description #1"
    assert len(category_1.products_list) == 2

    assert category_2.name == "Category #2"
    assert category_2.description == "Category description #2"
    assert len(category_2.products_list) == 1

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_file_not_found_error(mocker, caplog):
    """ Тестирование работы функции при отсутствующем файле. """
    mocker.patch("builtins.open", side_effect=FileNotFoundError)

    result = get_categories_objects_from_json("void.json")

    assert result is None
    assert "Нет такого файла: void.json" in caplog.text


def test_json_decode_error(mocker, caplog):
    """ Тестирование работы функции при ошибке парсинга. """
    mocker.patch("builtins.open", mock_open(read_data=json.dumps([{}])))
    mocker.patch("json.load", side_effect=json.JSONDecodeError('msg', 'doc', 0))

    result = get_categories_objects_from_json("void.json")

    assert result is None
    assert "Ошибка парсинга файла void.json" in caplog.text


def test_json_key_error(mocker, json_file_output, caplog):
    """ Тестирование обработки ошибки KeyError. """
    data = json_file_output
    del data[0]["name"]

    mocker.patch("builtins.open", mock_open(read_data=json.dumps(data)))
    mocker.patch("json.load", return_value=data)

    result = get_categories_objects_from_json("void.json")

    assert result is None
    assert "Отсутствует ключ: 'name'" in caplog.text


def test_unexpected_exception(mocker, caplog):
    """ Тестирование обработки непредвиденного исключения в основном блоке. """
    mocker.patch("builtins.open", side_effect=Exception("Симулированная ошибка"))

    result = get_categories_objects_from_json("void.json")

    assert result is None
    assert "непредвиденная ошибка: Симулированная ошибка" in caplog.text
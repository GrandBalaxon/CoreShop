# CoreShop

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📝 Описание

Учебный проект, разработанный в рамках изучения объектно-ориентированного программирования (ООП) на Python. 
Он представляет собой базовое ядро для системы электронной коммерции (e-commerce).

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.9 или новее
- Установленный pip

### Установка
1. Установите Poetry:
    ```bash
    pip install poetry
    ```
2. Установите [Git](https://git-scm.com/downloads/win).
3. Клонируйте репозиторий:
    ```bash
    git git@github.com:GrandBalaxon/CoreShop.git
    ```
    ```bash
    cd CoreShop
    ```
4. Установите зависимости проекта:
    ```bash
    poetry install
    ```

## 🔑 Настройка проекта

1. Поместите ваш JSON-файл с категориями продуктов в папку `data/`
   
## 🛠 Использование

### Запуск приложения

В проекте есть файл `main.py`, что не является точкой входа, а скорее временная затычка для проверки функционала работы
классов `Product` и `Category`.

```bash
python main.py
```

## ⚙️ Технические детали

### Логирование

* Вся работа функций в проекте логируется в `logs/application.log`
* Тесты логируются в `logs/tests.log`

## 🧪 Тестирование

Тестирование проекта реализовано через `pytest`

* Результаты тестов логируются в файле `logs/tests.log`
* Запуск тестов
    ```bash
    pytest
    ```
* Создание html-отчета о покрытие проекта тестами. Отчет будет сгенерирован в папке `htmlcov` и храниться в файле с названием `index.html`.
    ```bash
    pytest --cov=src --cov-report=html
    ```

## 📜 Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
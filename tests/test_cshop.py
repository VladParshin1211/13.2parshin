import pytest

from src.category import Product, Category


@pytest.fixture
def products():
    return [Product("Яблоко", "Россия", 10.99, 100),
            Product("Банан", "Импорт", 20.50, 50)]
@pytest.fixture
def category(products):
    return Category("Фрукты", "Производитель", products)
def test__init(category, products):
    assert category.name == "Фрукты"
    assert category.description == "Производитель"
    assert category.products == products
def test_product(category, products):
    assert Category.counter_product == 4

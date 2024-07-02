import pytest
from src.category import Category
from src.products import Product


@pytest.fixture
def category(product1):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [product1])


@pytest.fixture
def product1():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test__init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"

def test_category(category, product1):
    assert Category.total_categories == 1
    assert Category.counter_product == 1
    category.add_product(product1)
    assert Category.counter_product == 2


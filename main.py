from src.category import Category
from src.products import Product

category = Category('Смартфоны', "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [])
apple = Product.create_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      })
category.add_product(apple)


print(apple)
print(category.products)
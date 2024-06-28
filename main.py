from src.shop import Category, Product

category = Category()
apple = Product.create_product("Apple", 80, 15)
category.add_product(apple)


print(apple)
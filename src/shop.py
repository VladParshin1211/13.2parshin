class Category:
    name = str
    description = str
    product = list
    total_categories = 0
    counter_product = 0

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.products = product

        Category.total_categories += 1
        Category.counter_product += len(product)
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    @property
    def get_products(self):
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."


class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
        new_product = cls(name, description, price, quantity)
        return new_product

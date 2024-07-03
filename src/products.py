class Product:
    name = str
    description = str
    price = float
    quantity = int
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, prod_dict):
        name = prod_dict["name"]
        description = prod_dict["description"]
        price = prod_dict["price"]
        quantity = prod_dict["quantity"]
        new_product = cls(name, description, price, quantity)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("цена введена некорректная")
        else:
            self.__price = value


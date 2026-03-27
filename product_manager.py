from product import *

class ProductManager(Product):
    def __init__(self, name, price,quantity):
        super().__init__(name, price, quantity)
        self.shopping_history = []

    def total_spent(self) -> float:
        return sum(item.get_price() * item.quantity for item in self.shopping_history)

    def add_product(self, product : Product) -> None:
         self.shopping_history.append(product)

    def display_info(self) -> str:
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

from product import *

class ProductManager:
    def __init__(self):
        self.shopping_history = []

    def total_spent(self) -> float:
        return sum(item.price * item.quantity for item in self.shopping_history)

    def add_product(self, product : Product) -> None:
         self.shopping_history.append(product)

    def display_info(self) -> str:
        return f"shopping history: {self.shopping_history}"

    def remove_product(self, product: Product) -> None:
        self.shopping_history.remove(product)

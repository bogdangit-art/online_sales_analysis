from product import *

class Cart:
    def __init__(self):
        self.cart_items = []


    def add_products(self, product : Product) -> None:
         self.cart_items.append(product)

    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_info(self) -> str:
        return f'Name: {self.cart_items}\n Price: {self.total_price()}'






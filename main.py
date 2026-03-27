from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    products = [
        Product("Ochelari", 589.99, 1789),
        Product("Stilou", 124.49, 234),
        Product("Carte electronica", 44.45, 0),
        Product("Vioara acustica", 325.80, 765),
        Product("Boxa", 105, 100)
    ]


    for product in products:
        print(f"{product.name} in stock: {product.check_quantity()}")
        print(f"Total spent is: {product.price * product.quantity}")



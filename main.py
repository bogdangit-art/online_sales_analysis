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

    cart = Cart()

    cart.add_products(products[0])
    cart.add_products(products[1])
    cart.add_products(products[2])

    print(f"Total cart price is:", cart.total_price())
    print(f"Cart items are:", cart.display_info())




    for product in products:
        print(f"{product.name} in stock: {product.check_quantity()}")
        print(f"Total spent is: {product.price * product.quantity}")



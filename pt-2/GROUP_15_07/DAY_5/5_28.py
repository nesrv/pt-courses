class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart: # композиция или агрегация
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price


class Order: # композиция или агрегация
    def __init__(self, customer, shopping_cart):
        self.customer = customer
        self.shopping_cart = shopping_cart

    def checkout(self):
        total = self.shopping_cart.get_total_price()
        print(f"К оплате : {self.customer} : {total}")

product1 = Product("Футблока", 48)
product2 = Product("Кружка", 12)


shopping_cart = ShoppingCart()

shopping_cart.add_product(product1)
shopping_cart.add_product(product2)

order = Order("Алексей", shopping_cart)
order.checkout()
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List


# --- 1. Продукт ---
@dataclass
class Product:
    name: str
    price: float


# --- 2. Корзина товаров ---
@dataclass
class Cart:
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)

    def total_price(self) -> float:
        return sum(product.price for product in self.products)


# --- 3. Пользователь ---
@dataclass
class User:
    username: str
    email: str


# --- 4. Абстрактный класс для методов оплаты ---
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# --- 5. Конкретные реализации методов оплаты ---
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"[CreditCard] Charged ${amount:.2f} to credit card.")


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"[PayPal] Paid ${amount:.2f} via PayPal.")


class CryptoPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"[Crypto] Transferred equivalent of ${amount:.2f} in crypto.")


# --- 6. Заказ ---
@dataclass
class Order:
    user: User
    cart: Cart
    payment_method: PaymentMethod

    def process_order(self):
        total = self.cart.total_price()
        print(f"User {self.user.username} is placing an order worth ${total:.2f}")
        self.payment_method.pay(total)
        print("Order completed!")



laptop = Product(name="Laptop", price=999.99)
mouse = Product(name="Mouse", price=25.50)

# Пользователь
user = User(username="johndoe", email="john@example.com")

# Корзина
cart = Cart()
cart.add_product(laptop)
cart.add_product(mouse)

# Метод оплаты (можно заменить на PayPalPayment(), CryptoPayment())
payment = CreditCardPayment()

# Заказ
order = Order(user=user, cart=cart, payment_method=payment)
order.process_order()

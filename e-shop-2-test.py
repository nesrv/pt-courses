import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys

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


# --- Юнит-тесты ---
class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        """Тест создания продукта с корректными атрибутами"""
        product = Product(name="Test Product", price=10.99)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.99)


class TestCart(unittest.TestCase):
    def test_empty_cart(self):
        """Тест пустой корзины"""
        cart = Cart()
        self.assertEqual(len(cart.products), 0)
        self.assertEqual(cart.total_price(), 0)
    
    def test_add_product(self):
        """Тест добавления продукта в корзину"""
        cart = Cart()
        product = Product(name="Test Product", price=10.99)
        cart.add_product(product)
        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0], product)
    
    def test_total_price(self):
        """Тест расчета общей стоимости корзины"""
        cart = Cart()
        cart.add_product(Product(name="Product 1", price=10.50))
        cart.add_product(Product(name="Product 2", price=5.25))
        cart.add_product(Product(name="Product 3", price=7.75))
        self.assertEqual(cart.total_price(), 23.50)


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        """Тест создания пользователя с корректными атрибутами"""
        user = User(username="testuser", email="test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")


class TestPaymentMethods(unittest.TestCase):
    def setUp(self):
        # Перенаправляем stdout для проверки вывода
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        # Восстанавливаем stdout
        sys.stdout = self.original_stdout
    
    def test_credit_card_payment(self):
        """Тест оплаты кредитной картой"""
        payment = CreditCardPayment()
        payment.pay(100.00)
        self.assertIn("[CreditCard] Charged $100.00 to credit card.", self.held_output.getvalue())
    
    def test_paypal_payment(self):
        """Тест оплаты через PayPal"""
        payment = PayPalPayment()
        payment.pay(75.50)
        self.assertIn("[PayPal] Paid $75.50 via PayPal.", self.held_output.getvalue())
    
    def test_crypto_payment(self):
        """Тест оплаты криптовалютой"""
        payment = CryptoPayment()
        payment.pay(50.25)
        self.assertIn("[Crypto] Transferred equivalent of $50.25 in crypto.", self.held_output.getvalue())


class TestOrder(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.user = User(username="testuser", email="test@example.com")
        self.cart = Cart()
        self.cart.add_product(Product(name="Product 1", price=10.00))
        self.cart.add_product(Product(name="Product 2", price=20.00))
        
        # Создаем мок для метода оплаты
        self.payment_method = MagicMock(spec=PaymentMethod)
        
        # Перенаправляем stdout для проверки вывода
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        # Восстанавливаем stdout
        sys.stdout = self.original_stdout
    
    def test_process_order(self):
        """Тест обработки заказа"""
        order = Order(user=self.user, cart=self.cart, payment_method=self.payment_method)
        order.process_order()
        
        # Проверяем, что метод pay был вызван с правильной суммой
        self.payment_method.pay.assert_called_once_with(30.00)
        
        # Проверяем вывод
        output = self.held_output.getvalue()
        self.assertIn("User testuser is placing an order worth $30.00", output)
        self.assertIn("Order completed!", output)


class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Перенаправляем stdout для проверки вывода
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output
    
    def tearDown(self):
        # Восстанавливаем stdout
        sys.stdout = self.original_stdout
    
    def test_full_order_flow(self):
        """Интеграционный тест полного процесса заказа"""
        # Создаем продукты
        laptop = Product(name="Laptop", price=999.99)
        mouse = Product(name="Mouse", price=25.50)
        
        # Создаем пользователя
        user = User(username="johndoe", email="john@example.com")
        
        # Создаем корзину и добавляем продукты
        cart = Cart()
        cart.add_product(laptop)
        cart.add_product(mouse)
        
        # Проверяем общую стоимость
        self.assertAlmostEqual(cart.total_price(), 1025.49, places=2)
        
        # Создаем заказ с оплатой кредитной картой
        payment = CreditCardPayment()
        order = Order(user=user, cart=cart, payment_method=payment)
        
        # Обрабатываем заказ
        order.process_order()
        
        # Проверяем вывод
        output = self.held_output.getvalue()
        self.assertIn("User johndoe is placing an order worth $1025.49", output)
        self.assertIn("[CreditCard] Charged $1025.49 to credit card.", output)
        self.assertIn("Order completed!", output)


if __name__ == "__main__":
    unittest.main()
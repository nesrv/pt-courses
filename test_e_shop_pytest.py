import pytest
from io import StringIO
import sys
from unittest.mock import MagicMock

# Импортируем классы из файла e-shop-2-test.py
from e_shop_2_test import (
    Product, Cart, User, PaymentMethod, 
    CreditCardPayment, PayPalPayment, CryptoPayment, Order
)

# --- Тесты для класса Product ---
def test_product_creation():
    """Тест создания продукта с корректными атрибутами"""
    product = Product(name="Test Product", price=10.99)
    assert product.name == "Test Product"
    assert product.price == 10.99

# --- Тесты для класса Cart ---
def test_empty_cart():
    """Тест пустой корзины"""
    cart = Cart()
    assert len(cart.products) == 0
    assert cart.total_price() == 0

def test_add_product():
    """Тест добавления продукта в корзину"""
    cart = Cart()
    product = Product(name="Test Product", price=10.99)
    cart.add_product(product)
    assert len(cart.products) == 1
    assert cart.products[0] == product

def test_total_price():
    """Тест расчета общей стоимости корзины"""
    cart = Cart()
    cart.add_product(Product(name="Product 1", price=10.50))
    cart.add_product(Product(name="Product 2", price=5.25))
    cart.add_product(Product(name="Product 3", price=7.75))
    assert cart.total_price() == 23.50

# --- Тесты для класса User ---
def test_user_creation():
    """Тест создания пользователя с корректными атрибутами"""
    user = User(username="testuser", email="test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"

# --- Тесты для методов оплаты ---
@pytest.fixture
def capture_stdout():
    """Фикстура для перехвата стандартного вывода"""
    stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = stdout
    yield stdout
    sys.stdout = old_stdout

def test_credit_card_payment(capture_stdout):
    """Тест оплаты кредитной картой"""
    payment = CreditCardPayment()
    payment.pay(100.00)
    assert "[CreditCard] Charged $100.00 to credit card." in capture_stdout.getvalue()

def test_paypal_payment(capture_stdout):
    """Тест оплаты через PayPal"""
    payment = PayPalPayment()
    payment.pay(75.50)
    assert "[PayPal] Paid $75.50 via PayPal." in capture_stdout.getvalue()

def test_crypto_payment(capture_stdout):
    """Тест оплаты криптовалютой"""
    payment = CryptoPayment()
    payment.pay(50.25)
    assert "[Crypto] Transferred equivalent of $50.25 in crypto." in capture_stdout.getvalue()

# --- Тесты для класса Order ---
@pytest.fixture
def order_setup():
    """Фикстура для настройки заказа"""
    user = User(username="testuser", email="test@example.com")
    cart = Cart()
    cart.add_product(Product(name="Product 1", price=10.00))
    cart.add_product(Product(name="Product 2", price=20.00))
    payment_method = MagicMock(spec=PaymentMethod)
    return user, cart, payment_method

def test_process_order(order_setup, capture_stdout):
    """Тест обработки заказа"""
    user, cart, payment_method = order_setup
    order = Order(user=user, cart=cart, payment_method=payment_method)
    order.process_order()
    
    # Проверяем, что метод pay был вызван с правильной суммой
    payment_method.pay.assert_called_once_with(30.00)
    
    # Проверяем вывод
    output = capture_stdout.getvalue()
    assert "User testuser is placing an order worth $30.00" in output
    assert "Order completed!" in output

# --- Интеграционный тест ---
def test_full_order_flow(capture_stdout):
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
    assert pytest.approx(cart.total_price(), 0.01) == 1025.49
    
    # Создаем заказ с оплатой кредитной картой
    payment = CreditCardPayment()
    order = Order(user=user, cart=cart, payment_method=payment)
    
    # Обрабатываем заказ
    order.process_order()
    
    # Проверяем вывод
    output = capture_stdout.getvalue()
    assert "User johndoe is placing an order worth $1025.49" in output
    assert "[CreditCard] Charged $1025.49 to credit card." in output
    assert "Order completed!" in output

# --- Параметризованные тесты ---
@pytest.mark.parametrize("products,expected_total", [
    ([], 0),
    ([Product("Single Item", 10.0)], 10.0),
    ([Product("Item 1", 10.0), Product("Item 2", 20.0)], 30.0),
    ([Product("Item 1", 10.0), Product("Item 2", 20.0), Product("Item 3", 30.0)], 60.0),
])
def test_cart_with_different_products(products, expected_total):
    """Параметризованный тест корзины с разным количеством товаров"""
    cart = Cart()
    for product in products:
        cart.add_product(product)
    assert cart.total_price() == expected_total
## ✅ Техническое задание: Учебный интернет-магазин

 **Цель** : Создать упрощённую модель интернет-магазина для изучения объектно-ориентированного программирования на Python.

### 📚 Требования:

1. **Использование `@dataclass`** :

* Для описания продуктов (товаров).
* Для заказов и пользователей.

1. **Применение абстракции (ABC)** :

* Абстрактный класс `PaymentMethod` с методом `pay(amount: float)`.
* Несколько реализаций: `CreditCardPayment`, `PayPalPayment`, `CryptoPayment`.

1. **Применение полиморфизма** :

* Оплата заказа может происходить с использованием любого типа `PaymentMethod`.

---

## 🔧 Структура классов

* `Product` — товар (`@dataclass`)
* `Cart` — корзина, которая хранит товары и может рассчитывать общую сумму.
* `User` — пользователь (`@dataclass`)
* `Order` — заказ (содержит корзину, пользователя, метод оплаты)
* `PaymentMethod` (ABC) и его подклассы

---

## 🧠 Реализация с разбором

```python
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


# --- 🔍 Пример использования ---
if __name__ == "__main__":
    # Продукты
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
```

---

## 🧩 Разбор концепций

### ✅ `@dataclass`

* Упрощает создание классов с полями, например `Product`, `User`, `Cart`, `Order`.

### ✅ Абстракция

* `PaymentMethod` определяет, что каждый метод оплаты должен реализовать `pay()`.
* Это позволяет изолировать интерфейс от конкретной реализации.

### ✅ Полиморфизм

* Класс `Order` не знает, каким способом будет происходить оплата.
* Любой метод, реализующий `pay`, может быть подставлен: `CreditCardPayment`, `PayPalPayment`, `CryptoPayment`.

---

## 🧪 Доп. Идеи для развития

* Добавить скидки, налоги.


Отлично! Чтобы сделать реализацию скидок более гибкой и объектно-ориентированной, мы создадим:

* Абстрактный класс `Discount`
* Конкретные типы скидок, например:
  * `PercentageDiscount` — процентная скидка на всю корзину
  * `FixedAmountDiscount` — фиксированная сумма скидки
  * `ProductSpecificDiscount` — скидка на определённый товар

---

## ✅ Шаг 1: Абстрактный класс `Discount`

```python
from abc import ABC, abstractmethod
from typing import List

# Абстрактный класс для скидок
class Discount(ABC):
    @abstractmethod
    def apply(self, products: List[Product]) -> float:
        """Возвращает сумму скидки, применённой к списку продуктов"""
        pass
```

---

## ✅ Шаг 2: Реализации скидок

```python
# Скидка в процентах на всю корзину
class PercentageDiscount(Discount):
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, products: List[Product]) -> float:
        subtotal = sum(p.price for p in products)
        return subtotal * (self.percent / 100)


# Фиксированная сумма скидки
class FixedAmountDiscount(Discount):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, products: List[Product]) -> float:
        subtotal = sum(p.price for p in products)
        return min(self.amount, subtotal)  # Не больше, чем сумма товаров


# Скидка на определённый товар (по имени)
class ProductSpecificDiscount(Discount):
    def __init__(self, product_name: str, percent: float):
        self.product_name = product_name
        self.percent = percent

    def apply(self, products: List[Product]) -> float:
        discount = 0.0
        for p in products:
            if p.name == self.product_name:
                discount += p.price * (self.percent / 100)
        return discount
```

---

## ✅ Шаг 3: Изменим `Cart` для поддержки `Discount`

```python
@dataclass
class Cart:
    products: List[Product] = field(default_factory=list)
    discount: Discount = None  # теперь это объект Discount или None
    tax_percent: float = 0.0

    def add_product(self, product: Product):
        self.products.append(product)

    def subtotal(self) -> float:
        return sum(product.price for product in self.products)

    def discount_amount(self) -> float:
        if self.discount:
            return self.discount.apply(self.products)
        return 0.0

    def tax_amount(self) -> float:
        return (self.subtotal() - self.discount_amount()) * (self.tax_percent / 100)

    def total_price(self) -> float:
        return self.subtotal() - self.discount_amount() + self.tax_amount()
```

---

## ✅ Шаг 4: Использование

```python
if __name__ == "__main__":
    # Продукты
    book = Product(name="Book", price=30.0)
    pen = Product(name="Pen", price=5.0)

    # Пользователь
    user = User(username="alice", email="alice@example.com")

    # Выбор скидки
    discount = PercentageDiscount(10)  # Или: FixedAmountDiscount(5), ProductSpecificDiscount("Pen", 50)

    # Корзина
    cart = Cart(discount=discount, tax_percent=20)
    cart.add_product(book)
    cart.add_product(pen)

    # Оплата
    payment = PayPalPayment()

    # Заказ
    order = Order(user=user, cart=cart, payment_method=payment)
    order.process_order()
```

---

## 🔍 Преимущества такого подхода

* Используется **абстракция** через `Discount(ABC)`
* Поддерживается **полиморфизм** — можно подставлять разные типы скидок без изменения `Cart`
* Расширяемость: легко добавить новые типы скидок (например, "Купи 2 — получи 1 бесплатно")

---

Хочешь, чтобы скидки можно было комбинировать (например, сначала процент, потом фикс)?

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum
import uuid


# Использование Enum для категорий товаров - демонстрация типизации
class Category(Enum):
    ELECTRONICS = "Электроника"
    BOOKS = "Книги"
    CLOTHING = "Одежда"
    FOOD = "Продукты"


# Датакласс для товара - демонстрация датаклассов
@dataclass
class Product:
    name: str
    price: float
    category: Category
    product_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    description: str = ""
    stock: int = 0
    
    def __post_init__(self):
        # Валидация при создании объекта
        if self.price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if self.stock < 0:
            raise ValueError("Количество товара не может быть отрицательным")


# Специализированные товары - демонстрация наследования и расширения датаклассов

@dataclass
class ElectronicsProduct(Product):
    warranty_months: int = 12
    voltage: str = "220V"
    
    def __post_init__(self):
        super().__post_init__()
        self.category = Category.ELECTRONICS


@dataclass
class BookProduct(Product):
    author: str = ""
    pages: int = 0
    
    def __post_init__(self):
        super().__post_init__()
        self.category = Category.BOOKS


@dataclass
class ClothingProduct(Product):
    size: str = "M"
    color: str = "black"
    
    def __post_init__(self):
        super().__post_init__()
        self.category = Category.CLOTHING


# Абстрактный класс для скидок - демонстрация абстракции
class Discount(ABC):
    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """Применить скидку к товару и вернуть новую цену"""
        pass


# Конкретные реализации скидок - демонстрация полиморфизма
class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        if not 0 <= percentage <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self.percentage = percentage
    
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percentage / 100)


class FixedDiscount(Discount):
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма скидки не может быть отрицательной")
        self.amount = amount
    
    def apply_discount(self, product: Product) -> float:
        return max(0, product.price - self.amount)


class BuyOneGetOneDiscount(Discount):
    def apply_discount(self, product: Product) -> float:
        # Цена за единицу при покупке "1+1"
        return product.price / 2


# Абстрактный класс для платежных систем
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Обработать платеж на указанную сумму"""
        pass


# Конкретные реализации платежных систем
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # В реальном приложении здесь был бы код для обработки платежа
        print(f"Обработка платежа кредитной картой на сумму {amount}")
        return True


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Обработка платежа через PayPal на сумму {amount}")
        return True


# Датакласс для элемента корзины
@dataclass
class CartItem:
    product: Product
    quantity: int = 1
    
    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity


# Класс корзины покупок
class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Добавить товар в корзину"""
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        
        # Проверяем, есть ли уже такой товар в корзине
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        
        # Если товара нет, добавляем новый элемент
        self.items.append(CartItem(product, quantity))
    
    def remove_item(self, product_id: str) -> None:
        """Удалить товар из корзины"""
        self.items = [item for item in self.items if item.product.product_id != product_id]
    
    def update_quantity(self, product_id: str, quantity: int) -> None:
        """Обновить количество товара в корзине"""
        if quantity <= 0:
            self.remove_item(product_id)
            return
        
        for item in self.items:
            if item.product.product_id == product_id:
                item.quantity = quantity
                return
    
    def get_total(self) -> float:
        """Получить общую стоимость товаров в корзине"""
        return sum(item.total_price for item in self.items)
    
    def clear(self) -> None:
        """Очистить корзину"""
        self.items = []


# Датакласс для заказа
@dataclass
class Order:
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: List[CartItem] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    total_amount: float = 0
    status: str = "new"
    
    def __post_init__(self):
        if not self.items:
            raise ValueError("Заказ должен содержать хотя бы один товар")
        self.total_amount = sum(item.total_price for item in self.items)


# Класс интернет-магазина
class OnlineShop:
    def __init__(self, name: str):
        self.name = name
        self.products: Dict[str, Product] = {}
        self.orders: List[Order] = []
    
    def add_product(self, product: Product) -> None:
        """Добавить товар в каталог магазина"""
        self.products[product.product_id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Получить товар по ID"""
        return self.products.get(product_id)
    
    def list_products(self, category: Optional[Category] = None) -> List[Product]:
        """Получить список товаров, опционально фильтруя по категории"""
        if category:
            return [p for p in self.products.values() if p.category == category]
        return list(self.products.values())
    
    def create_order(self, cart: ShoppingCart, payment_processor: PaymentProcessor) -> Optional[Order]:
        """Создать заказ из корзины покупок"""
        if not cart.items:
            raise ValueError("Корзина пуста")
        
        # Проверяем наличие товаров на складе
        for item in cart.items:
            product = self.get_product(item.product.product_id)
            if not product or product.stock < item.quantity:
                raise ValueError(f"Недостаточно товара '{item.product.name}' на складе")
        
        # Обрабатываем платеж
        total_amount = cart.get_total()
        if not payment_processor.process_payment(total_amount):
            return None
        
        # Создаем заказ
        order = Order(items=cart.items.copy(), total_amount=total_amount)
        
        # Обновляем остатки на складе
        for item in cart.items:
            product = self.get_product(item.product.product_id)
            product.stock -= item.quantity
        
        self.orders.append(order)
        cart.clear()
        return order


# Пример использования
def main():
    # Создаем магазин
    shop = OnlineShop("TechShop")
    
    # Добавляем товары
    laptop = ElectronicsProduct(
        name="Ноутбук HP Pavilion",
        price=45000,
        category=Category.ELECTRONICS,
        description="Мощный ноутбук для работы и игр",
        stock=10,
        warranty_months=24
    )
    
    book = BookProduct(
        name="Python для начинающих",
        price=1200,
        category=Category.BOOKS,
        description="Лучшая книга для изучения Python",
        stock=50,
        author="Иван Иванов",
        pages=350
    )
    
    tshirt = ClothingProduct(
        name="Футболка Python Developer",
        price=1500,
        category=Category.CLOTHING,
        description="Стильная футболка для программистов",
        stock=30,
        size="L",
        color="blue"
    )
    
    shop.add_product(laptop)
    shop.add_product(book)
    shop.add_product(tshirt)
    
    # Создаем корзину и добавляем товары
    cart = ShoppingCart()
    cart.add_item(laptop)
    cart.add_item(book, 2)
    
    # Применяем скидку к товару
    discount = PercentageDiscount(10)
    discounted_price = discount.apply_discount(laptop)
    print(f"Цена ноутбука со скидкой: {discounted_price}")
    
    # Оформляем заказ
    payment_processor = CreditCardProcessor()
    order = shop.create_order(cart, payment_processor)
    
    if order:
        print(f"Заказ {order.order_id} успешно оформлен на сумму {order.total_amount}")
    else:
        print("Ошибка при оформлении заказа")


if __name__ == "__main__":
    main()
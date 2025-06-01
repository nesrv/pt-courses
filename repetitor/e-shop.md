## 📄 Техническое задание

### Интернет-магазин

1. реализовать классическим ООП
2. реализовать на датаклассах
 

### 📌 Основной функционал:

#### 1. **Каталог товаров**

* Класс `Product`

  * Поля: `name`, `price`, `stock`
  * Метод: `reduce_stock(quantity)`
  * Метод: `__repr__()` для отображения

#### 2. **Корзина покупателя**

* Класс `Cart`

  * Хранит словарь вида `{product: quantity}`
  * Методы:

    * `add_product(product, quantity)`
    * `view_cart()`
    * `get_total()`
    * `checkout()`

#### 3. **Пользователь**

* Класс `User`

  * Поля: `name`, `cart`
  * При создании пользователь автоматически получает корзину

#### 4. **Магазин**

* Класс `Store`

  * Хранит список товаров
  * Методы:

    * `add_product(product)`
    * `show_products()`
    * `get_product(index)`

### 💡Требования:

* Нельзя купить больше, чем есть в наличии.
* Нельзя оформить пустую корзину.


```py
# Пример Создаём магазин
store = Store()

# Добавляем товары
store.add_product(Product("Хлеб", 40, 50))
store.add_product(Product("Молоко", 70, 30))
store.add_product(Product("Яблоки", 100, 20))

# Показываем товары
print("🛒 Товары в магазине:")
store.show_products()

# Создаём пользователя
user = User("Алиса")

# Алиса кладёт в корзину товары
user.cart.add_product(store.get_product(0), 2)  # Хлеб x2
user.cart.add_product(store.get_product(2), 3)  # Яблоки x3

# Показываем корзину
print("\n📦 Корзина пользователя:")
user.cart.view_cart()

# Общая сумма
print(f"\n💰 Общая сумма: {user.cart.get_total()}₽")

# Оформляем заказ
total_paid = user.cart.checkout()
print(f"\n✅ Заказ оформлен на сумму {total_paid}₽")

# Снова показываем остаток товаров
print("\n🔁 Остаток товаров после покупки:")
store.show_products()

```


# Дополнительный функционал


### 🔄 **1. Удаление товара из корзины**

Добавить в `Cart` метод:

```python
def remove_product(self, product, quantity=None):
    ...
```

---

### 🔍 **2. Поиск товара в магазине по названию**

Добавить в `Store` метод:

```python
def search(self, keyword):
    ...
```

---

### 💸 **3. Баланс пользователя и оплата**

Добавить в `User` поле `balance`, метод `pay(total)`:

```python


    def pay(self, amount):
        if self.balance >= amount:
            ...
            return True
        else:
            ...  ValueError("Недостаточно средств")
```

Модифицировать `checkout()`:

```python
def checkout(self, user):
    total = self.get_total()
    ...
        return total
```

---

### 🧾 **4. История покупок**

Добавить в `User` поле `history`, сохранять туда кортежи `(product, qty, price)` после `checkout`.

---

### ⏱️ **5. Добавление сроков годности**

Добавить в `Product` поле `expiration_date`, и метод:

```python
def is_expired(self, current_date):
   ...
```

---

### 🎁 **6. Скидки и акции**

Добавить поле `discount_percent` и метод расчёта итоговой цены:

```python
def get_price(self):
    ...
```

---

### 🗳️ **7. Категории товаров**

Добавить в `Product` поле `category`. Добавить в `Store` метод `filter_by_category(category)`.

---

### 🛍️ **8. Пополнение склада**

Добавить метод `restock(self, amount)` в `Product`.

---


```py
from dataclasses import dataclass, field
from typing import Dict, List

# ---------- Классы ----------

@dataclass
class Product:
    name: str
    price: float
    stock: int

    def reduce_stock(self, quantity: int):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            raise ValueError("Недостаточно товара на складе")

    def __repr__(self):
        return f"{self.name} - {self.price}₽ (Stock: {self.stock})"


@dataclass
class Cart:
    items: Dict[Product, int] = field(default_factory=dict)

    def add_product(self, product: Product, quantity: int):
        if quantity > product.stock:
            raise ValueError("Недостаточно товара для добавления в корзину")
        self.items[product] = self.items.get(product, 0) + quantity

    def view_cart(self):
        for product, qty in self.items.items():
            print(f"{product.name} x{qty} = {product.price * qty}₽")

    def get_total(self) -> float:
        return sum(product.price * qty for product, qty in self.items.items())

    def checkout(self) -> float:
        total = self.get_total()
        for product, qty in self.items.items():
            product.reduce_stock(qty)
        self.items.clear()
        return total


@dataclass
class User:
    name: str
    cart: Cart = field(default_factory=Cart)


@dataclass
class Store:
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)

    def show_products(self):
        for idx, product in enumerate(self.products):
            print(f"{idx + 1}. {product}")

    def get_product(self, index: int) -> Product:
        return self.products[index]


# ---------- Тестовые объекты и действия ----------

# Создаём магазин
store = Store()

# Добавляем товары
store.add_product(Product("Хлеб", 40, 50))
store.add_product(Product("Молоко", 70, 30))
store.add_product(Product("Яблоки", 100, 20))

# Показываем товары
print("🛒 Товары в магазине:")
store.show_products()

# Создаём пользователя
user = User("Алиса")

# Алиса кладёт в корзину товары
user.cart.add_product(store.get_product(0), 2)  # Хлеб x2
user.cart.add_product(store.get_product(2), 3)  # Яблоки x3

# Показываем корзину
print("\n📦 Корзина пользователя:")
user.cart.view_cart()

# Общая сумма
print(f"\n💰 Общая сумма: {user.cart.get_total()}₽")

# Оформляем заказ
total_paid = user.cart.checkout()
print(f"\n✅ Заказ оформлен на сумму {total_paid}₽")

# Снова показываем остаток товаров
print("\n🔁 Остаток товаров после покупки:")
store.show_products()


```
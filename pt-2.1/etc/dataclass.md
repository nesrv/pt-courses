`@dataclass` в Python — это удобный способ создавать классы, в которых основная задача — хранение данных. Он автоматически создаёт конструктор (`__init__`), метод сравнения (`__eq__`), представление (`__repr__`) и другие полезные методы.

---

## 📦 Без `@dataclass`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## ✅ С `@dataclass`

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

Теперь ты можешь легко создать экземпляр:

```python
p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30)
```

---

## 🔁 Сравнение объектов

```python
p1 = Person("Bob", 25)
p2 = Person("Bob", 25)

print(p1 == p2)  # True (сравниваются по значениям, а не по ссылкам)
```

---

## 🧰 Дополнительные фишки

### Поля со значением по умолчанию:

```python
@dataclass
class Product:
    name: str
    price: float = 0.0

p = Product("Milk")
print(p)  # Product(name='Milk', price=0.0)
```

---

### Исключение из `__init__` (например, вычисляемое поле):

```python
from dataclasses import dataclass, field

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(3, 4)
print(r.area)  # 12




Отлично! Давай посмотрим на **более сложный пример**, в котором задействованы **дополнительные возможности `@dataclass`**, такие как:

* `field()`: управление полями (`init`, `repr`, `default_factory`)
* `__post_init__()`: дополнительная инициализация
* `order=True`: поддержка сортировки объектов
* вложенные `@dataclass`
* `frozen=True`: иммутабельные классы

---

## 🧠 Пример: Учёт заказов в интернет-магазине

```python
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

# Товар
@dataclass(order=True)
class Product:
    sort_index: float = field(init=False, repr=False)
    name: str
    price: float

    def __post_init__(self):
        # Используется для сортировки
        self.sort_index = self.price


# Заказ
@dataclass
class Order:
    products: List[Product]
    created_at: datetime = field(default_factory=datetime.now)
    total: float = field(init=False)

    def __post_init__(self):
        self.total = sum(p.price for p in self.products)

    def add_product(self, product: Product):
        self.products.append(product)
        self.total += product.price


# Пользователь
@dataclass(frozen=True)
class User:
    id: int
    name: str
```

---

## ✅ Использование:

```python
# Создаём товары
apple = Product("Apple", 1.5)
banana = Product("Banana", 0.9)
carrot = Product("Carrot", 0.7)

# Сортируем по цене
for p in sorted([apple, banana, carrot]):
    print(p)

# Создаём заказ
order = Order(products=[apple, banana])
print(f"Total before: {order.total:.2f}")

order.add_product(carrot)
print(f"Total after: {order.total:.2f}")

# Создаём пользователя (immutable)
user = User(id=1, name="Alice")
print(user)

# user.name = "Bob"  # ❌ вызовет ошибку, потому что frozen=True
```

---

## 💡 Что здесь использовано:

| Возможность                        | Что делает                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| `order=True`                       | Создаёт методы сравнения `<`, `<=`, `>` и `>=` на основе полей                |
| `sort_index` + `field(init=False)` | Скрытое поле для сортировки по цене, не участвует в `__init__` или `__repr__` |
| `__post_init__()`                  | Позволяет рассчитывать поля после создания                                    |
| `field(default_factory=...)`       | Позволяет задать значение по умолчанию (например, `datetime.now`)             |
| `frozen=True`                      | Делает объект неизменяемым                                                    |

---



Хорошо! Давайте развьём ваш пример, добавив в него полноценную ООП-структуру:

* Классы: `Human`, `RegistryOffice` (ЗАГС), `HouseholdBook` (Домовая книга).
* Логика: регистрация брака через ЗАГС, автоматическое изменение статуса и запись в домовую книгу.

---

### 🔧 Реализация на Python

```python
class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex.upper()  # 'M' or 'W'
        self.status = 'single'
        self.spouse = None

    def __str__(self):
        return f'{self.name} ({self.sex}), статус: {self.status}'

    def marry(self, partner, registry_office):
        registry_office.register_marriage(self, partner)


class RegistryOffice:
    def register_marriage(self, person1, person2):
        if person1.sex == person2.sex:
            print(f'❌ Брак между {person1.name} и {person2.name} невозможен (один пол).')
            return
        if person1.status != 'single' or person2.status != 'single':
            print(f'❌ Один из партнеров уже состоит в браке.')
            return

        person1.status = 'married'
        person2.status = 'married'
        person1.spouse = person2
        person2.spouse = person1
        print(f'✅ Брак зарегистрирован: {person1.name} и {person2.name}')


class HouseholdBook:
    def __init__(self):
        self.residents = []

    def register_resident(self, person):
        self.residents.append(person)
        print(f'👤 {person.name} добавлен(а) в домовую книгу.')

    def show_residents(self):
        print('📖 Домовая книга:')
        for person in self.residents:
            print(f'  - {person}')


# Использование
zags = RegistryOffice()
dombook = HouseholdBook()

ivan = Human('Иван', 'm')
anna = Human('Анна', 'w')

dombook.register_resident(ivan)
dombook.register_resident(anna)

# Женим
ivan.marry(anna, zags)

# Печатаем статусы
print(ivan)
print(anna)

# Показываем домовую книгу
dombook.show_residents()
```

---

### 🧠 Что это демонстрирует:

* **Инкапсуляция** : у каждого класса своя ответственность (люди, ЗАГС, книга).
* **Взаимодействие объектов** : люди взаимодействуют через посредника (ЗАГС).
* **Ограничения логики** : невозможность однополого брака или повторного брака.
* **Связи между объектами** : поле `spouse` устанавливается обоюдно.

---

Хочешь, можем добавить  **развод** ,  **детей** ,  **смерть** , **переезд** и т.д. — для тренировки ООП это отличная база.

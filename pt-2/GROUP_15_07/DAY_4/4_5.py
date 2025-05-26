# lambda + key + lst + str


lst = ["Москва", "Тверь", "Смоленск", "Псковь", "Рязань"]
lst.sort(key=lambda x: x[-1])
# print(lst)


books = (
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 500),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мертвые души", "Гоголь Н.В.", 190)
)

# books = sorted(books, key = lambda x : x[-1])
books = sorted(books, key = lambda x : (x[2], x[1]))
print(*books, sep='\n')
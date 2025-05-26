def look(words):
    match words:
        case {"red": "красный"| "фуксия" | "бордовый"}:
            print("red и его оттенки есть в словаре")
        case {"blue": "синий"} | {"green": "зеленый"}:
            print("или или")
        case {}:
            print("Слова red и blue в словаре отсутствует")
        case _:
            print("все остальное") #словарь или все остальное (4)


look({"red": "красный", "blue": "синий", "green": "зеленый"})

look({"red": "красный", "green": "зеленый"})

look({"blue": "синий", "green": "зеленый"})

look({"green": "зеленый"})

look({"red": "оранжевый", "blue": "синий" })
look({"red": "бордовый", "blue": "синий" })
look({"red": "фуксия" })

look("yelllow")
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str

anne = Person(first_name="Anne",
              last_name="Smith",
              age=40,
              job="software engineer",)


# print(anne)

from functools import singledispatch

@singledispatch
def fun(arg):
    print("1 аргумент:", arg)


@fun.register(int)
def _(arg):
    print("Вызов числом")

@fun.register(list)
def _(arg):
    print("Вызов списком")

fun('привет')
fun(1)
fun([1, 2, 3])

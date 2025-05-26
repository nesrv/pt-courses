class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()

tb1.name = 'Франция'
tb1.days = 6

tb1.total_blogs += 1

tb2 = TravelBlog()
tb1.name = 'Италия'
tb1.days = 5

TravelBlog.total_blogs += 1
TravelBlog.total_blogs += 1
TravelBlog.total_blogs += 1

delattr(tb1, 'total_blogs')

res = tb1.total_blogs
res2 = tb2.total_blogs


# print(res)
# print(res2)

class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()

fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

# delattr(fig1, 'color')
# print(*fig1.__dict__)
#
# print(fig1.type_fig)


class Person:
    name = 'Иван Иванов'
    job = 'Программист'
    city = 'Москва'


p1 = Person()

print(hasattr(p1, "job"))
print("job" in p1.__dict__)
print(p1.__dict__)

from  json import dumps
from collections import Counter, namedtuple

class MyCounter:

    def __init__(self, text):
        self.text = text.strip().replace(",","")


    def simple_counter(self):
        temp = {}
        for word in self.text.split():
            temp[word] = self.text.count(word)
        return dumps(temp, indent=2)


    def __repr__(self):
        return self.text

f = open("txt.txt")

s = f.read()
# my_count = MyCounter(s)
# print(my_count.simple_counter())
#
# print(Counter(s.replace(",","").split()))
# print(Counter(s.replace(",","").split()).most_common()[0][0])


def counter_by_namedtuples(text):
    name = namedtuple('name', ['word', 'count'])
    temp = {tuple(name(word, text.count(word))) for word in text.strip().split()}
    print(*temp)



counter_by_namedtuples(s)
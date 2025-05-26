class Indexator:

    def __init__(self, stop_words):
        self.stop_words = stop_words


    def __call__(self, string):
        return ' '.join(filter(lambda w :  w not in self.stop_words, string.lower().split()))

    def my_filter(self, string):
        return ' '.join(filter(lambda w :  w not in self.stop_words, string.lower().split()))

list_of_stop_words = ["в", "и", "по", "за", "на"]

string_to_process = ("Сервис по поиску работы и сотрудников "
                     "HeadHunter опубликовал подборку"
                     " высокооплачиваемых вакансий в России за ноябрь 2024 года"
                     "в Москве. На первых строчках IT-архитекторы и техлиды  ")


my_indexator = Indexator(list_of_stop_words)


# res = my_indexator(string_to_process)
res = my_indexator.my_filter(string_to_process)

print(res)
# бинарная сериализация ?
# pickle

import pickle


class Virus:

    def __init__(self):
        print("я вирус")

    def __call__(self, *args, **kwargs):
        print("я размножаюсь")
        open("virus.txt", "w")




virus = Virus()


# with open('pickle_virus', 'wb') as f:
#     pickle.dump(virus, f)



input_file = open('pickle_virus', 'rb')
func = pickle.load(input_file)

func()


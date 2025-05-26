import numpy as np

a = np.array([1, 2, 3, 4])

print (a.dtype)

a = np.array([1, 2, "3", True])
print (a)
print (a.dtype)

a = np.array([1,2,3,4,5,6,7,8,9])

print (a[ [1,1,1,1,1,1,1,1,1] ])

print (a[ [3,3,3] ])

b = a.reshape(3, 3)

print(b)

print(b[0, 0])
print(b[0][ 1])


def getList():
    for i in range(10):
        yield i
 
a = np.array( [x for x in getList()] )
print(a)


# Объявление многомерных массивов

a = np.array([[1, 2], [3, 4], [5, 6]])

# a = np.array([[1, 2], [3, 4], [5, 6, 7]]) # ошибка


np.array( [0]*10 )  # массив из 10 нулей
np.array( [1]*15 )  # массив из 15 единиц
np.array( [x for x in range(10)] ) # массив из чисел от 0  до 9

np.empty(10) # создание одномерного массива с произвольными числами
np.empty(10, dtype='int16')
np.empty((3, 2), dtype='float32') # возвращаетматрицу 3x2 стипомfloat32


np.eye(4)    # матрица 4х4
np.eye(4, 2)         # матрица 4x2
np.identity(5) # матрица 5x5


np.zeros( (2, 3, 4) ) # нулевая матрица размерностью 2x3x4
np.ones( [4, 3], dtype='int8') # матрица 4x3 из единиц и типом int8
np.full((3, 2), -1) # матрица 3x2, состоящая из -1


np.asmatrix('1 2 3 4') # создает матрицу 1x4 из строки
np.asmatrix('1, 2, 3, 4') # то же самое: создает матрицу 1x4 из строки
np.asmatrix('1 2; 3 4') # возвращает матрицу 2x2
import numpy as np
# # # a = np.array([1, 2, 3, 4])
# # # a = np.array([1, 2, "3", True])
# # # print(a.dtype)
# # # a[0]=123
# # # print(a[0])
# # # print(a[-1])
# # # print(a)

# # a = np.array([1,2,3,4,5,6,7,8,9])

# # print (a[ [2,2,2]])
# # print (a[ [1,1,1,1]])


# # b = a.reshape(3,3)

# # print(b)
# # print('-'*20)
# # print(b[1][1])
# # print('-'*20)
# # print(b[1,1])
# # print('-'*20)

# # a = np.array([1,2,3,4], 'str_')
# # # float16,32,64
# # # int8-64
# # # uint8-64
# # # bool
# # # complex64, 128, complex_
# # # str
# # print(a)
# # a = np.array([x**3 for x in range(10)], 'str_')
# # print(a)

# # Объявление многомерных массивов

# a = np.array([[1, 2], [3, 4], [5, 6]])

# # a = np.array([[1, 2], [3, 4], [5, 6, 7]]) # бага

# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# print(b[0])
# print(b[0,0,0])

# a = np.array([0] * 10)
# a = np.array([1] * 15)

# print(a)
# a = np.empty(10, dtype='int8')
# a = np.empty((3,2), dtype='float')
# a = np.eye(4,2, dtype='int8')
# a = np.identity(5)
# a = np.zeros((2,3,4))
# a = np.ones((4,5), dtype='int8')
# a = np.ones([4,5], dtype='int8')

# print(a)

# # Функции создания матриц

# a = np.asmatrix('1 2 3 4') # создает матрицу 1x4 из строки
# print(a)
# a = np.asmatrix('1, 2, 3, 4') # создает матрицу 1x4 из строки
# a = np.asmatrix('1 2; 3 4') # создает матрицу 2x2 из строки
# print(a)

# a = np.diag([1, 2, 3])
# print(a)

# a = np.diag([(1,2,3), (4,5,6), (7,8,9)]) 
# выделение элементов главной диагонали
# print(a)

# a = np.diagflat([(1,2,3), (4,5,6), (7,8,9)]) 
# выделение элементов главной диагонали
# print(a)

# a = np.tri(4)
# print(a)

# a = np.tri(4,2)
# print(a)

# a = np.array( [(1,2,3), (4,5,6), (7,8,9)] )

# print(np.tril(a))
# print(np.triu(a)) # # верхняя треугольная матрица размером 3x3

# print(np.tril([[[1,2,3], [4,5,6], [7,8,9]]]))
# двумерные сечения будут приведены к треугольному виду.


# формирования числовых диапазонов

# range(Start, Stop, Step)
# arange()

a = np.arange(5)# интервал [0; 5) с шагом 1
a = np.arange(1, 5, 0.5)# интервал [0; 5) с шагом 0.5
a = np.arange(0, np.pi, 0.5)# интервал [0; 5) с шагом 0.5
print(a)
b = np.cos(a)
print(b)

# linspace(start, stop, …)
# разбивает указанный интервал на равномерные отрезки

b = np.linspace(0, np.pi, 5)
print(*b, sep='\n')
print("-" * 20)
# Функции logspace (логариф кривая) и geomspace

a = np.logspace(0, 1, 3) # 1, sqrt(10), 10
print(*a, sep='\n')
print("-" * 20)
a = np.logspace(0, 1, 4)
print(*a, sep='\n')

print("-" * 20)
a = np.geomspace(1, 4, 3)
print(*a, sep='\n')

print("-" * 20)
a = np.geomspace(1, 16, 5)
print(*a, sep='\n')
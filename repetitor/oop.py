##
## OOP
# зачем
# __init__ конструктор
# __str__
# __repr__
# __len__
# __iter__

from math import dist

print(dist((3,4,0),(0,0,0)))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __len__(self):
        return int(dist((self.x, self.y), (0, 0)))
    
    def __hash__(self):       
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return dist((self.x, self.y), (0, 0)) < dist((other.x, other.y), (0, 0))
    
    
    def __le__(self, other):
        return self.__len__() <= other.__len__()
      
    
class Point3D(Point):  
    def __init__(self, x,y,z):    
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return super().__repr__()[:-1] +  f',{self.z})'
  

p1 = Point(3,4)
p2 = Point3D(1,2,3)
p3 = Point(3,4)


print(p1 == p3)
# print(hash(p1), hash(p3))


d = {}
d[p1]='p1'
d[p2]='p2'
d[p3]='p3'

print(p3 >= p1)


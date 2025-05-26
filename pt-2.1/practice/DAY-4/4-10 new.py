class Point:
    count = 0

    def __new__(cls):
        cls.count += 1
        if cls.count > 2:
            print('кол-во подкючений ограничено')

        else:

            return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('точка создана')
        self.x = x
        self.y = y




p1 = Point()
p2 = Point()
p3 = Point()

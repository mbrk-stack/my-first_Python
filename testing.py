# les bases de la p.o.o
# les classes en python
# class Nom_class {
#   constructor(attriobuts)
#   methodes
# }

class Point:
    total = 0
    # __x:float
    def __init__(self, x:float, y:float):
        self.__x = x
        self.y = y
        Point.total +=1
    # getter (accesseur en consultation)
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x:float):
        self.__x = x

    def getX(self):
        return self.__x
    
    def setX(self, x:float):
        self.__x = x

    def add(self):
        return self.__x + self.y
    
    # class method
    @classmethod
    def addcls(cls, p):
        return p.x + p.y
    
    @classmethod
    def getTotal(cls):
        return cls.total
    
    @staticmethod
    def hello():
        print("hello point")
    
    def __str__(self):
        return f"X : {self.x}, Y : {self.y}"
    
    
# Héritage

class Livingthing:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Nom:{self.name} Age:{self.age}"  
    
class Human(Livingthing):
    def __init__(self, name:str, age:int, sexe:str):
        super().__init__(name, age) 
        self.sexe = sexe
        
    def __str__(self):
        return f"{super().__str__()}, Sexe:{self.sexe}"

if __name__ == "__main__":
    p1 = Point(12,8)
    # plist:list[Point] = [p1, Point(34,9), Point(8,12)]
    print(p1.getX())
    print(p1.x)
    p1.x = 89
    p1.setX(45)
    print(p1.getX())

    # for point in plist:
    #     print(point.y)
    # print(plist)
    # t.add() faux
    # r = p1.add()
    # r1 = Point.add(p1)
    # rcls = Point.addcls(p1)
    # total = Point.getTotal()
    # Point.hello()
    # f = Point.add
    # r1 = f(p1)
    # print(r1)
    # print(rcls)
    # print(total)
    # print(f"point : {p1}, somme : {r}")
# les bases de la p.o.o
# les classes en python
# class Nom_class {
#   constructor(attributs)
#   methodes
# }

class Point:
    
    def __init__(self, x:float, y:float):
        self.__x = x
        self.__y = y

    def add(self):
        return self.__x + self.__y
    
    @property        #getter 
    def x(self):
        return self.__x
    
    # if you dont want to write the @ you can create a methode and define what you want to do
    
    @x.setter
    def x(self, w):
        self.__x = w
    
    # class method
    @classmethod
    def addcls(cls, p):
        return p.x + p.y
    

    def __str__(self):
        return f"X : {self.__x}, Y : {self.__y}"
    

if __name__ == "__main__":
    p1 = Point(12,8)
    plist:list[Point] = [p1, Point(34,9), Point(8,12)]
    print(p1.x)

    p1.x = 89
    print(p1.x)
    
    # for point in plist:
    #     print(point.y)
    # print(plist)
    # t.add() faux
    # r = p1.add()
    # r1 = Point.add(p1)
    # rcls = Point.addcls(p1)
    # f = Point.add
    # r1 = f(p1)
    # print(r1)
    # print(rcls)
    # print(p1.y)
    # print(f"point : {p1}, somme : {r}")
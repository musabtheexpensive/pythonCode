from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(shape):
    def area(self):
        area = 0.5*self.dim1 * self.dim2
        print("Area of Triangle:",area)

class Rectangle(shape):
    def area(self):
        area =self.dim1 * self.dim2
        print("Area of Rectangle:",area)

t1=Triangle(20,50)
t1.area()

r1=Rectangle(60,40)
r1.area()
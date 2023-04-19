import random
import math as mth



class Circle(Geom):
    
    def __init__(self,r): #area method for a circle
        self.radius = r
        super().__init__()
        
    def area(self):
        return mth.pi * self.radius **2
        
circle_list = [Circle(i) for i in range(2,4)] #create a list of circles with radius 2 and 3
print(circle_list)

for x in circle_list:
    x.print_name()
print([x.makestring() for x in circle_list])

class Square(Geom):
    
    def __init__(self,s): #area method for a square
        self.side = s # s= side
        super().__init__()
        
    def area(self):
        return self.side **2
s = 8
my_square = Square(s)
my_square.print_name()
print('My area is ',my_square.area())

class Triangle(Geom):
    
    def __init__(self,bh): #area method for a square
        self.side = bh 
        super().__init__()
        
    def area(self):
        return (mth.sqrt(3)/ 4)*(self.side **2) # square root of 3/2 times x^2
    
triangle_list = [Triangle(k) for k in range(7,15)] #create a list of triangles with sides 7- 14
print(triangle_list)

for z in triangle_list:
    z.print_name()
print([z.makestring() for z in triangle_list])

bh = 10
my_triangle = Triangle(bh)
my_triangle.print_name()
print('My area is ',my_triangle.area())
  


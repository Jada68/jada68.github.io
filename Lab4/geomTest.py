import shapely.geometry as geom
from shapely.geometry import Point

myCircle = geom.Circle([1,2,])

point1 = Point([0, 0])
point2 = Point([5, 5])
point3 = Point([6, 7])

myTriangle = Triangle([10])
print(my_triangle.area())
import math
class Line:

    def __init__(self,coor1,coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        global x1,y1
        global x2,y2

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def slope(self):

        return (y2-y1) / (x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

class Cylinder:

    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius

    def volume(self):

        return math.pi * ((self.radius)**2) * self.height

    def surface_area(self):

        top = math.pi * (self.radius)**2
        return (top*2) + (2 * math.pi * self.radius * self.height)

mycyl = Cylinder(2,3)
print(mycyl.volume())
print(mycyl.surface_area())






    



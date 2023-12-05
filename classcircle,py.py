import math
class circle:
    def __init__(self,radius):
        if isinstance(radius,(int,float)):
            if radius<0:
                self.radius=0
            else:
                self.radius=radius
    def getRadius(self):
        print("Raadius of circle",self.radius)
    def getArea(self):
        area=self.radius*self.radius*math.pi
        print("Area of circle:",area)
class cylinder(circle):
    def __init__(self,radius,height):
        self.height=height
        super().__init__(radius)
        if isinstance(height,(int,float)):
            if height<0:
                self.height=0
            else:
                self.height=height
    def getHeight(self):
        print("Height of cylinder:",self.height)
    def getVolume(self):
        print("volume of Cylinder:",self.radius*self.radius*math.pi*self.height)
c1=cylinder(6,12)
c1.getRadius()
c1.getHeight()
c1.getArea()
c1.getVolume()
print("-- radius and height less than 0 then theresult iss:--")
c=cylinder(-6,-12)
c.getRadius()
c.getHeight()
c.getArea()
c.getVolume()
print("pull")

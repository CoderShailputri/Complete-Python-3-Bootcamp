#Day Eight OOP Assignment
#Assignment 1 - Find distance and slope of line
print("\n\nAssignment 1 - Find distance and slope of line")
class Line : 
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2
	def distance (self):
		return ((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2)**0.5
	def slope(self):
		return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])

coor1 = (3,2)
coor2 = (8,10)
l = Line(coor1,coor2)
print("The distance of the line given the coordinates is : {}".format(l.distance()))

print("The slope of the line given the coordinates is : {}".format(l.slope()))






#Assignment 2 - Find volume and surface area of a cylinder of given radius 
print("\n\nAssignment 2 - Find volume and surface area of a cylinder of given radius")
class Cylinder:
	pi = 3.14
	def __init__(self, height = 1, radius = 1):
		self.height = height
		self.radius = radius
	def volume(self):
		return Cylinder.pi*self.radius*self.radius*self.height
	def surface_area(self):
		return (2*Cylinder.pi*self.radius*self.height) + (2*Cylinder.pi*self.radius**2)

c = Cylinder(2,3)
print("The volume of cylinder is: {}".format(round(c.volume(),2)))
print("The total surface area of cylinder is: {}".format(round(c.surface_area(),2)))

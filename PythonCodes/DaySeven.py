#DaySeven
#Object Oriented Programming (OOP)
class NameofClass(): #Classes Camel Casing. For functions we use snake casing.
	def __init__(self,param1,param2):#called a method when inside of class
		self.param1 = param1
		self.param2 = param2
	def other_method(self):
		print(self.param1)

#Creating user defined objects
class Dog():
	#Creating attributes (char of object)
	#inside the class it is called method
	#self connects method to instance of class
	def __init__(self,breed, name, spots=None): #constructor for class #byconvention instace of class is called self
		'''
		Expecting breed, name and spots'''
		self.breed = breed #assignining passed value to attribute
		self.name = name
		#self.spots = spots
	def bark(self,number):
		print("Woof! My name is {} and the no is {}".format(self.name, number)) #Even here it is self.name
		

print("\n\nDemonstrating class attribute and method Example 1")
my_dog = Dog(breed = 'lab', name = 'Sammy', spots = False)
print(my_dog.name) #Class Attribute
print(my_dog.bark(10)) #Class Method
#help(Dog)


#Class object attributes
class Circle():
	pi = 3.14 #Attribute
	def __init__(self,radius=1): #creating an instance of class
		self.radius = radius
	def get_circumference(self): #creating a method of class
		return self.radius*self.pi*2 #we can also write Circle.pi instead of self.pi

my_circle = Circle(30)
print("\n\nDemonstrating class attribute and method Example 2")
print("The circumference is {}".format(my_circle.get_circumference()))

#Inhertiance - new classes using classes that have already been defined
class Animal():
	def __init__(self):
		print("Animal Created")
	def who_am_I(self):
		print("I am an animal")
	def eat(self):
		print("I am eating")

class Cat(Animal): #Cat is an inherited class of Animal
	def __init__(self):
		Animal.__init__(self)
		print("Cat created")
	def eat(self):
		print("I am a Cat and eating")

#my_animal = Animal()
mycat= Cat()
print("\n\nDemonstrating class inhertiance")

print(mycat.who_am_I()) #Cat class uses all attributes and methods of the Animal class
print(Animal().eat())


#Polymorphism - When 2 classes share the same method name
class Dog():
	def __init__(self,name):
		self.name = name
	def speak (self):
		return self.name + " says Woof"
class Cat():
	def __init__(self,name):
		self.name = name
	def speak (self):
		return self.name+ " says meow"
niko = Dog("niko")
jennu = Dog("Jennu")
felix = Cat("felix")
Caty = Cat("Caty")

def pet_speak(pet):
	print(pet.speak())

print("\n\nDemonstrating class polymorphism")
for PeT_name in [niko,jennu,felix,Caty]:
	pet_speak(PeT_name)

#Abstract Classes - Instance is not created. Serves only as base class
class Animal1():
	def __init__(self,name):
		self.name = name
	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method")

class Dog1(Animal1):
	def speak(self):
		return self.name + " Says woof!"
class Cat1(Animal1):
	def speak(self):
		return self.name+ " Says meow!"
fido = Dog1("Fido")
isis = Cat1("isis")
print("\n\nDemonstrating class abstraction")
print(fido.speak())
#print(Animal1.speak("Hatrick")) - This is an abstract class as we dint write Animal1.__init__(self) within Cat1 and Dog1

#Special Methods, Dunder / Magic methods

class Book():
	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages
	def __str__(self): #Can print user defined methods
		return f"{self.title} by {self.author}"
	def __len__(self): #Length of user defined methods
		return len(self.title)
	#def __del__(self): #if you remove the hash then every time an instance of the class is created, the below print statement will work
		#print("A book record has been deleted")

b= Book("Python Programming", "Jose", 200)
print("\n\nDemonstrating magic/special class")
print(b)
print("Length of the book name is: {}".format(len(b)))
#del b #Delete variable from computer memory
#print(b)

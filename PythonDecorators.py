#PythonDecorators - Change functionality of a function using ON/OFF switch
'''
@some_decorator
def simple_func():
	#Simple stuff
	return sth'''

def func():
	return 1

def hello():
	return "Hello!"

greet = hello

print(greet())

#Despite deleting hello(), greet would point to object hello

def hello1(name = 'Jose'):
	print ('Hello function executed!')

	def greethello():
		return "\t This is the greet() under hello()"

	def welcome():
		return "\t This is welcome() inside hello()"

	#print(greethello()) #One cannot call greet and welcome outside the functions
	#print(welcome())

	print("End of hello1")

	if name == 'Jose':
		return greethello() #Function can return a function
	else:
		return welcome()


print(hello1('123'))

print("\nDefining and returning the function")
def cool():
	def supercool():
		return "I am very cool!"
	return supercool()

print(cool())

print("\nFunction as an argument")
def hello2():
	return "Hi Jose!"
def other(some_def_func): #passing function as argument
	print("Other code runs here")
	print(some_def_func())

other(hello2) #No paranthesis

print("\nCreating a decorator")
def new_decorator(original_func):
	def wrap_func():
		print("Some extra code before the original function")
		original_func()
		print("Some extra code after the original function")
	return wrap_func()

def func_needs_decorator():
	print("I want to be decorated!")

print(new_decorator(func_needs_decorator))

print("\nDirectly using decorator")
@new_decorator #Used in django and flask in web development. Render a new website or point to another page
def func_needs_decorator1():
	print(" I want to be decorated!!!!!!!!!!!!")



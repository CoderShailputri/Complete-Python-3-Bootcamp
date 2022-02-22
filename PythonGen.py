#Python Generators - yield, next, iter
'''
Generators are functions that use yield instead of return as the output of the function is not stored in a list. Rather it returns single value every time function is called.'''

print("\n Using generators to create cubes")
def create_cubes(n):
	for x in range(n):
		yield n**3

print(create_cubes(10))
print(list(create_cubes(10)))

print("\nThis will generte fibonnacci series")
def gen_fibon(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a,b = b, a+b

for num in gen_fibon(10):
	print(num)

print("\n next keyword")
def simple_gen():
	for x in range(3):
		yield x

for num in simple_gen():
	print(num)

#next
print("\nNext keyword")
g = simple_gen()
print(next(g))


#iter
print("\nIter keyword")
s = 'Hello'
for letter in s:
	print(letter)

#next(s) #Cant do
s_iter = iter(s)
next(s_iter)

print("\nProblem 1 - Square of numbers")
def square_num (n):
	for num in range(n):
		yield num**2


num = 2
#input("Enter number:")
print(list(square_num(int(num))))

print("\nProblem 2 - Generate random numbers")
import random

def rand_num(low,high,n):
	while n>0:
		yield random.randint(low,high)
		n = n-1
	
for num in rand_num(1,10,12):
	print(num)

print("\nProblem 3 - Use of iter tp convert string to an iterable")
a = 'Hello'
a_iter = iter(a)
print(list(a_iter))


print("\n Generator comprehension to generate a list with one item at a time")
my_list = [1,2,3,4,5,6]
filter_list = [item for item in my_list if item > 3]
filter_gen = (item for item in my_list if item > 3)
print(filter_list == list(filter_gen))



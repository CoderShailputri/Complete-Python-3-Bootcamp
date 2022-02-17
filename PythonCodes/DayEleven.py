#Day Eleven - Errors and Exception handling


#try except finally
print("\n\nThis is a new block of code")
def add(n1,n2):
	print(n1+n2)
add(10,20)

'''num1 = 10
num2 = input("Enter number:")
add(num1,num2) #Will result in type error
print("Something happened") #This will not get executed'''

#using error handling in this program
print("\n\nThis is a new block of code")
try:
	#result = 10+'10' #will result in error
	result = 10+10
except :
	print("String input is causing an error") #This runs
else : #will execute only when there is no error
	print("All went well")
	print(result)

#Try except and finally
print("\n\nThis is a new block of code")
try: #try to attempt
	f = open('testfile','r')
	f.write("Write a test line") #Trying to write on a read only file
except TypeError:print("There was a tyoe error") #error
except OSError: print("Hey you have an OS Error")
except : print(
	"All other exceptions")
finally: print("I always run") #Always runs`

print("\n\nThis is a new block of code")
def ask_for_int(number):
	while True:
		try:
			result = int(number)
			#int(input("Please provide no:"))
		except:
			print("This is not a number")
			break
		else: 
			print("This is a number")
			break
		finally:
			print("End of try/except/finally")

ask_for_int('Please')

#Assignment
print("\n\nAssignment 1 in error handling")
try:
	set_a = ['a','b','c']
	set_b = [1,2,3]
	c = []
	for ele in set_b:
		c.append(ele**2)
except:
	print("You have entered string input")
else:
	print("You set of squares is {}".format(c))

#Assignment
print("\n\nAssignment 2 in error handling")
try:
	x=5
	y=0
	z=x/y
except:
	print("Result is Infinity")
else:
	print("Result is {}".format(z))
finally:
	print("All Done!")
	

print("\n\nAssignment 3 in error handling")
def ask():
	i = 0
	while i<2:
		try:
			num = int(input("Enter an integer: "))
		except:
			print("You have not entered an integer.")
			print("You have {} tries left".format(1-i))
			i = i+1
			continue
		else:
			print("You have entered {}".format(num))
			break
		finally:
			print("All done!")

ask()

#to run PyLint : pylint myexample.py -r y
#Unit Testing
a = 1
b = 2
print(a)
print(B)

#How to score better with pylint

'''

Descriptio here

'''

def myfunc():
    '''
    '''
    first = 1
    second = 2
    print(first)
    print(second)
my_func()

#Unittest library
def cap_text(text):
	'''
	Input string. Output capitalise the initials

	'''
	#return text.capitalize() #Capitalises single letter and not the entire string
	return text.title()

'''
---------------------------For testing -------------------------------------
In another .py script write such as TestingScreipt.py : 
import unittest
import DayEleven #importing a file

class TestCap(unittest.TestCase): #TestCase is class in built in package unittest
	def test_one_word(self):
		text = 'python'
		result  = DayEleven.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiple_words(self):
		text = 'Monty Python'
		result = DayEleven.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__  == '__main__':
	unittest.main()
'''



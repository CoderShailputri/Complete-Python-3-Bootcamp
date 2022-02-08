#Day 2 : Section 4, 5, 6
#Comparison operators AND, OR, NOT
print (not (1==1))
#-------------------------------------------------------------------
#Python Statements : Control Flow (if, elif, else), loops(for,while)
name = 'Sammy'
if name == 'Frankie':
	print ("Hello Frankie")
else:
	print ("Whats your name?")
#-------------------------------------------------------------------
#Tuple unpacking using for loop
my_list = [(1,2),(3,4),(5,6),(7,8)]
for a,b in my_list: #here we can also write (a,b)
	print (a)
	print (b)
	print (a,b)
#Dictionary unpacking using for loop
my_dict = {'k1': 1, 'k2':2,'k3':3}
for key,value in my_dict.items():
	print (value)
for ele in my_dict:
	print (ele) #only prints the keys!! To find values you need d.items() or d.values()
#-------------------------------------------------------------------
#use of pass, continue and break in for/if
name = 'Sammy'
for char in name:
	pass #used as a place holder here. Otherwise python shows error if nothing is mentioned in for
print('Enf of Code')
for char in name:
	
	if char == 'a':
		continue #this means that wen a is encountered, no action is taken and it goes back to for loop
	print (char)
x= 0
while x<5 :
	if x == 2:
		break
	print (x)
	x = x+1
#-------------------------------------------------------------------
#other operators : range,enumerate, zip, , min and max to find min/max in list
for ele in range(2,10,2):
	print (ele)
print(list(range(0,10,2)))
#enumerate takes any string/list and returns the tuple of index,char
word = 'abcde'
for char in enumerate(word):
	print (char)
for key,char in enumerate(word):
	print (char)
#zip together 2 lists [1,2,3], [a,b,c] into tuples. If extra items in one list, zip will ignore the extra items
mylist1 = ['a','b','c']
mylist2 = [1,2,3]
for item in zip(mylist1,mylist2):
	print (item)
print('mykey' in {'mykey':123})
d= {'mykey':123}
print(123 in d.values())
#-------------------------------------------------------------------
#random library
from random import shuffle
mylist = [1,2,3,4,5,6,7]
shuffle(mylist)
print(mylist)
from random import randint
a = randint(0,100)
print(a)
#var = input('Enter a no: ')
#print (int(var))
#-------------------------------------------------------------------
#for loop in list comprehensions
myword = 'Skeep'
mylist = [char for char in myword]
print(mylist)
squareno = [num**2 for num in range(0,11) if num%2==0]
print (squareno)
#The above is the same as writing
squareno = []
for num in range(0,11):
	if num%2 !=0:
		continue
	else:
		squareno.append(num**2)
print (squareno)
#when using if else in list comprehensions the order changes if-else comes before for as below:
result = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(result)
#nested loop in list comprehensiosn
my_list_num = [x*y for x in [2,4,6] for y in [1,10,100]]
print(my_list_num)
#-------------------------------------------------------------------
#Assignment Questions Here :
st = 'Print only the words that start with s in this sentence'
#Code here
print ('Test Starting here')
i=1
words = st.split()
for word in words:
  if word[0] == 's':
    print (f'{i}th word is :{word}')
    i+=1
print([x for x in range(0,11) if x%2 == 0])
mylist = [x for x in range(1,51) if x%3==0]
print(mylist)
st = 'Print every word in this sentence that has an even number of letters'
#Code in this cell
words = [st.split()] #this gives a list in a list. Therefore this will screw up the CODE!!!
words = st.split()
print (words)
for word in words:
	if len(word)%2 == 0:
		print(word)
	
for ele in range(1,101):
	if ele%15 == 0: #alternatively you could use: if ele % 3== 0 and ele%5 == 0
		print ("FizzBuzz")
	elif ele%3 == 0:
		print ("Fizz")
	elif ele%5 == 0:
		print ("Buzz")
	
	else:
		print (ele)
st = 'Create a list of the first letters of every word in this string'
#Code in this cell

mystring = [word[0] for word in st.split()]
print (mystring)

x = [range(0,11,2)] #this is not going to create a list usnless there is a for or something
x = list(range(0,11,2)) #this is going to create a list
print (x)
#-------------------------------------------------------------------
#looking for help/python documentation 
#help(mylist.insert) #so to see documentation using help do not type insert()
#-------------------------------------------------------------------
#Functions
#snake casing in functions and camel casing in classes (OOPs)
#return does not have (), unlke print
def say_hello (name='Default'): #so there is no error if no argument is passed when function is called
	print (f'Hello {name}')
	return None
say_hello()
#using function to unpack tuples
inputis = [('Abby',100),('Billy',800),('Cassie',400)]
def employee_check(work_hours):
	t = 0
	temp = 'Default'
	for emp,hours in work_hours:
		if t<hours : 
			t=hours
			temp = emp
		else : pass #this line is optional
	return(temp,t)
employee,timing = employee_check(inputis)
print (employee)
#3 cup Monte game

def randomise():
	mylist = [0,1,1]
	from random import shuffle
	shuffle(mylist) #it wont be mylist.shuffle() as this is an in place function that does not return anything
	print (f'The list is: {mylist}')
	for t,ele in enumerate(mylist):
		if ele == 0:return t
	else:pass


def Guess_the_place(position):
	if position == randomise():
		print ('You won!')
	else:
		print ('You lost!')


guess = ''
while guess not in ['0','1','2']:
	#guess = input('What is your guess 0,1 or 2? ')
	guess = '1'
Guess_the_place(int(guess))

#alternately you could have used functions to capture plyer guess and shuffle list and used a check_guess function
#-------------------------------------------------------------------
#args and kwargs or key word arguments
print ("R U THERE???")
def myfunc (*args): #pass any no of arguments user wants 
	print (args) #args is used by convention. * is the imp part here
	print (f'Number of arguments passed by user is : {len(args)}')
	print (sum(args))
myfunc(40,60)

def myfunc(**kwargs): #** means it is dictionary
	if 'fruit' in kwargs :
		print ('My fruit of choice is:{}'.format(kwargs['fruit'])) #kwargs['fruit'] is to capture the value of key fruit. 
	else :
		print ('I did not find fruit here')
myfunc(fruit = 'apple',veggie = 'Tomato')

def myfunc(*args,**kwargs): #first args and then kwargs. It cannot be the other way around
	print ('I would like {} {}'.format(args[0],kwargs['food']))
myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')

#practice qn to convert even place letter to upper case and odd place letter to lower case
def myfunc(mystring):
	i = 0
	newstring = []
	for char in mystring:
		if i%2 == 0:
			newstring.append(char.upper())
		else:
			newstring.append(char.lower())
		i = i + 1
	stringis = ''.join(newstring)
	print (stringis)
	return stringis
myfunc("awesome")


#more sleeker way is below : 
def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

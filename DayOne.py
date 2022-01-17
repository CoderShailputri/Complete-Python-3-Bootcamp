#Day1 
#Section 1 and 2 talked about different setups 
#Python environments : 
#IDE (PyCharm and Spyder), Text editors (Sublimetest and Atom is by Git), Notebooks (Jupyter - Use either Anaconda Navigator or https://jupyter.org/try)

#Uses of Python :
#Data Analysis (Numpy and Pandas), Visualisations (seaborn and matplotlib), ML (scykit-learn and pytorch), website development (Djando, Flask - backends and …)

#Section 3 : Working on Data types and Structures in Python
#----------------------------------------------------------------------------------
#Strings, Integers and Floating Point
a = "Hello World"
b = 1.1234987
print(a) #print the string
print(a[-3]) #string indexing
print(a[::-1]) #string reversing
print(a[2:-2:2]) #string slicing and reseversing
print(a[2:5:2]) #string slicing
print ('tinker'[1:4]) #slicing w/o assigning a variable
print ('The {} {} {}.'.format('crazy', 'fox', 'brown')) #how to use .format
print ('The {1} {1} {1}.'.format('crazy', 'fox', 'brown'))
print ('The {0} {2} {1}.'.format('crazy', 'fox', 'brown'))
print(f'Message says {a} !')
print ('Message says %s' %'Pooja') #using %s
print ('Message says :'+a) #String Concatenation
print ('The no is {r:1.2f}'.format(r=b)) #Truncating floating using .format
#Strings and list differ as strings are immutable, lists are mutable.
#object.method()...method() are basically functions. Objects is a data type like list/string
# Why doesn't 0.1+0.2-0.3 equal 0.0 ? - It has to do with how floating points are stored.
# PEP8 : Global variable names in all caps. Other variables all lower case.
#-----------------------------------------------------------------------------------------------
#Lists - Here we do indexing, slicing, reassignment, append(item), pop(index), sort(), reverse()
#pop and append both happen at the end
my_list = [1,'pooja',2.4,['Hero','Honda']]
new_list = [4,99,0,1,1,1,1,1,1]
print('Indexing1:{} indexing2: {}'.format(my_list[2],my_list[3][1]))
new_list.sort()
print (new_list)
new_list.reverse()
print (new_list)
my_list.append('P')
print(my_list)
my_list.pop(-2)
print(my_list)
my_list.append(['Hero','Honda'])
print(my_list)
#-----------------------------------------------------------------------------------------------
#Dictionaries - Used to stored unordered items retrieved by key. It cant be indexed, sliced or sorted
my_dict = {'apples':100, 'banana':50, 'kiwi':65, 'toothpaste 20g': 30, 'lock':[1,3,6]}
print('Dict output:{}'.format(my_dict['lock'][1]))
my_dict ['new_data']=999 #note that a new data appends at the end. Also there is use of '='' not ':''
print(my_dict)
print (my_dict.keys()) #to print only the keys
print (my_dict.values()) #to print only the values
print(my_dict.items()) #to print both keys and values
# dictionaries are useful to store a number of data variable types and retrieve by the KEYYYYYYYY!!!!!
#Be Careful while calling nested dictionary
#Grab hello in d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#d['k1'][0]['nest_key'][1][0]
#-----------------------------------------------------------------------------------------------
#Tuples - Like lists but it is immutable so used in large codes. Has only 2 methods associated with it count() and index()
my_tuple = (1,'banana',3.4, 1)
print(my_tuple.index(3.4))
print(my_tuple.count(1))
#-----------------------------------------------------------------------------------------------
#sets - are unordered collection of UNIQUE elements
my_set = set()
my_set.add('1') #this is the method to add to the set
my_set.add(2)
print(my_set)
print(set(new_list)) #this gives only unique values in the list
# set is written as {1,2,3}. [1,2,3] is a list
#-----------------------------------------------------------------------------------------------
#read(), seek(0), readlines(), open(), close()
myfile = open("/Users/pranshumaan/Downloads/PythonCodes/test.txt")
myfile.close()
with open("/Users/pranshumaan/Downloads/PythonCodes/test.txt") as my_file:
	contents = my_file.read()
print(contents)
with open ("/Users/pranshumaan/Downloads/PythonCodes/test.txt", mode = 'a') as f:
	f.write('\nThird Line') #this appends the existing file test.txt
x = open ("new_file", mode= 'w') #this creates a new text file
x.write('Creating new file')
x.close()
print ((2**2)*(50-25)+(1/4))
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print (d['k1'][2]['k2'][1]['tough'][2])
#---------------------------------------------------------------
#Booleans : True False and None
print(3.0 == 3) # This is True
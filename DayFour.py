#Day 4
#Challenging Problems
print("CHALLENGING PROBLEMS")
print("\n")
#SPY GAME
def spy_game(nums):
	# applied the wrong logic
	# for i in range(len(nums)):
	# 	if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
	# 		return True
	# 	else: continue
	# return False

	#PROGRAM THAT RUNS WITH RIGHT LOGIV HERE

	# i =0
	# j=0
	# ticker = []
	# while (i<len(nums)):
	# 	if nums[i]==0 or nums[i]==7:
	# 		ticker.append(nums[i])
	# 	i = i+1
	# print(ticker)
	# p = [False,False,False]
	# i=0
	# j=0
	# while (i<len(ticker)):
	# 	if ticker[i] == 0: 
	# 		p[j] = True
	# 		j=j+1
	# 		if j==2 : break
	# 	i = i+1
	# 	#print (i)
	# if 7 in ticker[i+1::]:
	# 		print ("Yes")
	# else:
	# 		print("No")

	
	#TRYING SOMETHING HERE
	i=0
	j=0
	while (i<len(nums)):
		if nums[i] == 0: 
			
			j=j+1
			if j==2 : break
		i = i+1
		
	if 7 in nums[i+1::]:
		return True
	else:
		return False

	#LOGIC USED IN ANSWER
	# code = [0,0,7,'x']
	# for num in nums:
	# 	if num == code[0]:
	# 		code.pop(0)
	# return len(code)==1

#TESTING
print(f'Q1 - Answer of spy game is: {spy_game([1,0,2,4,0,0,5,7])}')
# spy_game([1,0,7,2,0,7,5,0])
# spy_game([1,7,2,0,4,5,0])
# spy_game([1,0,2,4,0,5,7])


# capture = spy_game([0,0,7,0,7,0,5])
# print(f'Q1 - Result of spy game is:{capture}')

#COUNT PRIMES
def count_primes(num):
	
	

	i=3
	count = 0
	if num <2:
		count = -1 #To check if input is 0 or 1
	while i<=num:
		tick = True
		for j in range(2,i):
			#print (f'{i}/{j}')
			if i%j == 0: 
				tick = False
				break
			else : continue
		#print (f'tick is {tick}')
		if tick==True : 
			count = count + 1
			#print(f'Count value is:{count}')
		i = i + 1
	count = count + 1 
	print (f'Q2 - Total number of primes upto and including {num} is : {count}')

count_primes(1)
print("\nChallenging Problems over \n\n\n\n")
#Lamda, map and Filter
#Map (func,list) by itself returns a memory location.
# so do list(map(func,mylist)) Do not add () to the func you pass here
# list(filter(func,mylist))- filters the mylist based on criteri and returns the true cases
#can also use for to find the elements in map and filter functions
# lambda is an anonymous function for one time. labda num : num **2. It is used in conjunction with map or filter

 #Using lambda to grab first character of every word in list
mynames = ['Andy','Beauty','Cady','Dorothea']
print(f'Application of map and lambda : {list(map(lambda mynames:mynames[0],mynames))}')

#Nested Statements and Scope
#L(Local within def)E(Enclosing function)G(Global)B(Built in)

#Local - lambda num:num**2
name = "Global string"#this is global 
def greet():
	name = "Sammy"#here name is enclosing function
	def hello():#defining name here will be local
		print('Hello'+name)
	hello()
print(greet())	

x = 50
def func():
	global x
	x = 'NEW VALUE'
	print(f'Changed value: {x}') #changes global value of x
print(x)
func()
print(x)

#Functions and Methods Homework
print("\n\nFunctions and Methods Homework\n\n")
#Write a function that computes the volume of a sphere given its radius.
import math
def vol(rad):
	return (4/3*math.pi)*(rad**3)

print(f'Q1 - Volume of sphere is :{vol(2)}')


#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
	return low<num<high

r = ran_check(5,1,2)
print(f'Q2 - The given number is in range:{r}')

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
	words = s.split()
	count_up = 0
	count_down = 0
	# This is to find words starting with upper or lower case
	# for word in words:
	# 	if word[0].isupper():
	# 		count_up = count_up+1
	# 	if word[0].islower():
	# 		count_down = count_down+1
	# return count_up,count_down
	#To find how many upper and lower case characters are there
	for word in words:
		for char in word:
			if char.isupper():count_up = count_up+1
			elif char.islower(): count_down = count_down+1
	return count_up,count_down
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(f'Q3 - The number of upper and lower case words are:{up_low(s)} respectively')

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
	new_list = list(set(lst))
	return new_list
print(f'Q4 - The unique list is {unique_list([1,1,1,1,2,2,3,3,3,3,4,5])}')

#Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
	result = 1
	for ele in numbers:
		result = result * ele
	return result
print(f'Q5 - The multiplication result is: {multiply([1,2,3,-4])}')

#Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
	text = list(s.replace(" ",'').lower())
	new_text = text.copy() #cannot use assignment new_text = text here. Else after text reversal, new_text also gets reversed!!!
	text.reverse()
	return text == new_text
print (f'Q6 - Word is palindrome:{palindrome("nurses run")}')
#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(" ",'').lower()
    str1 = set(str1)
    return str1 == alphaset
print(f'Q7 - Pangram : {ispangram("The quick brown fox jumps over the lazy dog")}')
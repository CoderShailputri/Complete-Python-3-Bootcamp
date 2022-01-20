#Day 3 Section 6 & 7 - Practice Exercises and Milestone Project
#Warmup Section
print ("WARMUP PROBLEMS NOW !!!!!!!!!!!!!!!!!")
print ("\n")
#Q1 - LESSER OF TWO EVENS
def lesser_of_two_evens (a,b):
	if a%2 == 0 and b%2==0: #Both numbers are even
		return min(a,b) #Checking Lesser of evens
	else: return max(a,b) #Checking Greater as either number is odd
x = lesser_of_two_evens (2,5)
print (f'Q1 - Lesser of two evens {x}')
#Q2 - ANIMAL CRACKERS
def animal_crackers (mystring):
	words = mystring.lower().split() #convert everything to lower case so there is no false in case of upper/lower case
	return words[0][0] == words[1][0]
print(f'Q2 - Does initials match? {animal_crackers("Crazy Kangaroo")}')
#Q3 - MAKES TWENTY
def makes_twenty (n1,n2):
	return n1+n2 ==20 or n1==20 or n2==20 #sum() takes only list as argument
	
print(f'Q3 - Does it make twenty? {makes_twenty(2,3)}')
print ("\n\n")
#Level 1 Problems
print ("LEVEL 1 PROBLEMS NOW !!!!!!!!!!!!!!!!!")
print("\n")
#Q1 - Old Macdonald
def old_macdonald(name):
	new_name = []
	#print (len(name))
	for ele in range(len(name)):
		if ele == 0 or ele==3:
			new_name.append(name[ele].upper()) #String re-assignments like new_name[ele] = name[ele] do not work!! use append.
		else: new_name.append(name[ele])
	return ''.join(new_name)
print(f'Q1 - Macdonalding this:{old_macdonald("macdonald")}')
#Sleeker way of wiritng the above wo creating a new string 
# first_half = name[0:3]
# second_half = name[3:]
# return first_half.capitalise()+second_half.capitalise()
#Q2 - MASTER YODA
def master_yoda (text):
	words = text.split()
	new_text = words.reverse() #or reverse_word_list = wordlist[::-1]
	#print(' '.join(words))
	return ' '.join(words)

print (f'Q2 - Master Yoda says : {master_yoda ("I am home")}')
#Q3 - ALMOST THERE
def almost_there(n):
	n = abs(n)
	return 90<=n<=110 or 190<=n<=210 #Better way to do this (abs(100-n))) <= 10
print(f'Q3 - Is no almost 100 or 200? {almost_there(150)}')
print ("\n\n")
#LEVEL 2 Problems
print ("LEVEL 2 PROBLEMS NOW !!!!!!!!!!!!!!!!!")
print ("\n")
#Q1 - FIND 33
def has_33(nums):
	t = 0
	for ele in nums:
		if t==ele : 
			return True
		else: t=ele
	return False
print(f'Q1 - Is 33 together?{has_33([1,3,1])}')
# Sleeker way to do this
# for i in range(0,len(nums)-1):
# 	if nums[i] == 3 and nums[i+1]==3: reutrn True. Another Alternative is.. if nums[i:i+2]== [3,3]: reutrn True
# return False
#Q2 - PAPER DOLL
def paper_doll(text):
	new_text = [] #could have directly stored a string new_text = ''
	for char in text:
		new_text.append(char*3) #new_text += char*3
	return ''.join(new_text) #return new_text 
print(f'Q2 - The Paper doll output is:{paper_doll("Hello")}')

#Q3 - BLACK JACK
def blackjack(a,b,c):
	if a+b+c <= 21 : return a+b+c
	elif (a+b+c >21) and (a==11 or b==11 or c==11): return a+b+c-10 #could write if 11 in [a,b,c]
	elif (a+b+c) > 21 : return "BUST"
	else: return "NOTA"
print(f'Q3 - The blackjack result is: {blackjack(9,9,9)}')

#Q4 - SUMMER OF '69'
def summer_69(arr):
	new_arr = []
	i = 0
	while i < len(arr):
		if arr[i] == 6:
			#print ("Correct")
			while (arr[i] !=9):
				i = i+1
				#print (arr[i])
		new_arr.append(arr[i])
		i = i + 1
		#print (i)
		
	return sum(new_arr)-9
print(f'Q4 - the sum of summer_69 is:{summer_69([4,5,6,7,8,9])}')

print ("\n\n")
#Challenging Problems
print ("CHALLENGING PROBLEMS NOW !!!!!!!!!!!!!!!!!")
print ("\n")
#Q1 - SPY GAME


#Q2 - COUNT PRIMES
# def count_primes(num):
# 	count = 0
# 	for i in range(3,num+1):
# 		for j in range(2,i-1):
# 			if i%j != 0:
# 			else :
# 				# print ("Not prime")
# 				# return None
# 		#count = count+1
# 	return count
		
# z = count_primes(100)
# if z != None: print (f'Count is: {z}')
#Q3 - PRINT BIG



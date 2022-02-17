#Day5 Grab user input, Return adjusted variable



row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']

def display_func(row1, row2,row3):
	print (row1)
	print(row2)
	print(row3)


def validating_input(r,c):
	acceptable_range = range(0,3)
	if r.isdigit() == True and c.isdigit() == True and int(r) in acceptable_range and int(c) in acceptable_range:
		#here 0<=int(r)<=2 does not work why???
		print ("Inputs received")
		return True
	else:
		print ("Type input")
		return False



def get_input():
	
	r = 'WRONG'
	c = 'WRONG'
	while validating_input(r,c) == False: 
		r = input("Please choose row position: ") #you cannot pass a string here as strings cannot be changed?
		c = input("Please choose column position: ")
		var = input("X or O?: ")
	return int(r),int(c), var
	# if validating_input (r,c) == None:
	# 	return int(r),int(c)
	# else: get_input()

def put_func():
	row, column, var = get_input()
	if row == 0 : 
		row1[column]=var
	elif row == 1:
		row2[column]=var
	elif row == 2:
		row3[column]=var
	display_func(row1,row2,row3)


def play_game():
	cont = 'Y'
	t= 0
	cont = input("Do you want to play Y or N:? ")
	while cont == 'Y' and t<10:
		put_func()
		t = t+1
		cont = input("Do you want to still play Y or N:? ")
	else:
		print ("Game Over")
		return None

play_game()




 
		


#Checking if input is integer, else return an error using try...except
'''try:
    val = int(userInput)
except ValueError:
    print("That's not an int!")'''

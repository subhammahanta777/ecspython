''' 
def func_name():
    #do whatever 


'''


# creating a claculator to find add , sub, div, mul,mod,sq

def addition(a,b):
	add = a+b
	print(add)
def sub(a,b):
	sub = a-b
	print(sub)
def div(a,b):
	div = a/b
	print(div)
def mul(a,b):
	muly = a*b
	print(muly)
def mod(a,b):
	mod = a%b
	print(mod)
def sq(a):
	a = 10
	sq = a*a
	print(sq)
def user_input():
	a=int(input("please provide the first number"))
	b =int(input("please provide the second number"))
	return a,b



while True:
	user_choice=input("please select an option\n1.Add\n2.sub\n3.mul\n4.div\n")
	if (user_choice=='1'):
		a,b=user_input()
		addition(a,b)
	elif(user_choice =='2'):
		a,b=user_input()
		sub(a,b)
	elif(user_choice=='3'):
		a,b=user_input()
		mul(a,b)
	elif(user_choice=='4'):
		a,b=user_input()
		div(a,b)
	else:
		print("give correct input")









'''

output:


















'''
























'''
While loop 

syntax for while loop:

while (condition):
	do something



	update condition




'''

# # print your name 10 times
# i=10
# while i>0:
# 	print('subham',i)
# 	i = i-1

'''
take a number from the user and 
find the fact of the number using while loop
'''
while True:
	try:
		num = int(input("enter num ->\t"))
		i=1
		mul=1
		while i<= num:
			mul = mul * i
			i=i+1
		print (mul)
	except ValueError:
		print("Decimal values not accepted")


		


























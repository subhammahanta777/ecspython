''' Input : Name and current age
    output : year when he turns 100 '''


def cal_yr(age):
	current_yr=2017
	yrs_to_100 = 100-age
	yr_100=current_yr + yrs_to_100
	return yr_100
while True:
	user_input = input('please enter your name and age seperated with spaces\t-->\t')
	inp=user_input.split()
	if len(inp)==0:
		print("Please provide an input you dummy")
		continue
	name = inp[:-1]
	name = ' '.join(name)
	age = inp[-1]
	try:
		age = int(age)
	except ValueError:
		print("Invalid Age")
		continue
	if age >= 0 and age<100:
		yr = cal_yr(age)
		print("Hi %s you will 100 on %s"%(name, yr))	
	elif age<0:
		print("You are not born yet")
	elif age>100:
		yr = cal_yr(age)
		print("Hi %s you were 100 on %s"%(name, yr))
	elif age == 100:
		print("congratulations on your 100th year")
	else:
		



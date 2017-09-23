
# WAP to identify if a person can marry
#conditions for male - age limit - 21
#conditions for female - age limit - 18
while True:
	gender = input ("Give gender ->\t")
	age= int(input ("Give age ->\t"))
	gender= ''.join(gender.split())
	if (gender =='male' and age >= 21):
		print ("You Can")
	elif(gender =='male' and age < 21):
		print("You cannot")    
	elif(gender =='female' and age >= 18):
		print("you can")
	elif(gender =='female' and age < 18):
		print("You cannot")
	else:
		print("Gender or age mismatch")

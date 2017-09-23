'''

lists

syntax:

list_name = [ ]
len()

syntax for loop:
for <variable_name> in <some_collection_of_data>:
	do something


'''

# groceries = ['Daal','Rice','Sambar masala',1,2.5,'100gms']
# i = len(groceries)-1
# while i>=0:
# 	print (groceries[i])
# 	i = i-1

# for ele in groceries:
# 	print (ele)

# ## print numbers from 1 to 50 using for loop

# for idx,i in enumerate(range(100,111)):
# 	print (idx,i)

'''
create 2 lists of same size 
name the first list gro
name the second weights
finally print the gro's and their associated weights
together.
do it using enumerate
'''


groceries = ['Daal','Rice','Sambar masala']
weights = [1,2.5,'100gms']

'''
output : 
Daal 1
Rice 2,5
Sambar masala 100gms
'''

# for idx,ele in enumerate(groceries):
# 	print(ele+' '+str(weights[idx]))

list1 = [1,2,3,4,5,6]
list2=[1,0,3,5,4,6]
final_list=[]
for idx,i in enumerate(list1):
	if i == list2[idx]:
		final_list.append(True)
	else:
		final_list.append(False)

print(final_list)

# output : [True, False, True, False, False, True]



















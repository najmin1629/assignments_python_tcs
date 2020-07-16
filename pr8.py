def split(list): 
    return [char for char in list]  
list = 'ACADGILD'
print(split(list))

######

listtimes = range(1,5)
listletter = ['x','y','z']
print([i*j for i in listletter for j in listtimes])

#####

input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print(str(result))

#####

input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print(str(result))

#####

input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print(str(result))

#####

input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print(str(result))
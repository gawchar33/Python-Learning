# you can create tuple with just , seperated things it will create  the tuple so the parenthesis in the tuple are optonal 
my_tuple=(4,2,7)
print(my_tuple[2])# keep in mind [] this means json array and () this means object all the time so dont give the index in this 
a,b,c=my_tuple
print(f"the value of a , b , c is {a},{b},{c}")

c_tuple=2,4,6,7,2,4,3,2
print(c_tuple)
print(c_tuple.count(2))# method used to count how many time 2 comes in the tuple 
print(c_tuple.index(6))#  it will return the first index of occurance of 6 

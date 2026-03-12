# traditional way to iterate some function on all the elements 
number=[2,6,4,3]
result=[]
for n in number:
    result.append(n*n)
print(result)

#map way to apply the same thing on all the elements 
num=[3,7,8,5]

def mul(n):
    return n*n
result=map(mul,num)# this will give the memory location of the map 
result=list(map(mul,num)) # here we convert it into the list 
print(result)


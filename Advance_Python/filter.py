# traditional way to filter the even numbers 
num=[2,3,4,5,6,7,8]
result=[]
for n in num:
    if n%2==0:
        result.append(n)


print(result)

# filter high level function method to perform same thing 

nums=[2,3,5,6,7,8]
result=[]
result=list(filter(lambda x:x%2==0, nums))
print(result)

# filtering the string
names = ["Alice","Bob","Andrew","Tom"]

result = filter(lambda x: x.startswith("A"), names)

print(list(result))
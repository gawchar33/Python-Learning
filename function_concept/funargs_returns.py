#type of arguments in python 
#1.Positional argument
#2.Default arguments
#3.Keyword arguements

#1.positional argument

def add(a,b):
    return a+b
print(add(3,4))

#2.default arguments

def greeting(name="Friends"):
    return f"Hell0 {name}"# if u seperate this with , python will create the tuple here 
greet=greeting()
print(greet)

#keyword arguments
def add(a,b,c=10):
    return f"the sum of a,b and the default argument c is {a+b+c}"
sum=add(b=1,a=4,c=0)# when i provide the value here python override the value in default argument and give the sum of numbers 
# and if u didn't provide any value python will  take the default value and write down the sum
print(sum)
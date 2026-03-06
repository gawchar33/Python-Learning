'''4. String Formatting and f-Strings
Using format(), create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.

Do the same using f-strings.'''

#without f-string normal , way
name="Govind"
age=24
print("my name is ",name,"and my age is ",age)
#using format method
print("my name is {} and my age is {}".format(name,age))
print("my name is {0} and my age is {1}".format(name,age))#we can also use index to specify the position of the variable in the string
print("my name is {a} and my age is {b}".format(a=name,b=age))#we can also use index to specify the position of the variable in the string
print("my name is {b} and my age is {a}".format(a=name,b=age))#we can also use index to specify the position of the variable in the string    
#using f-strings            
    
print(f"my name is {name} and my age is {age}")
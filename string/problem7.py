#Write a program that counts how many vowels are in a given
print("hello world govind is here")
sentence = input("enter the string:")
#sentence = input("Enter the string:").lower()
#vowels="a,e,i,o,u"

vowels="A,E,I,O,U,a,e,i,o,u"

count=0

for ch in sentence:
    if ch in vowels:
        count+=1


print("the count of vowels in the sentence is ",count)
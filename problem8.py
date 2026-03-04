'''1.Print numbers from 1 to 10 using a while loop.
2.Write a program that keeps asking the user to enter a password until they
enter the correct one.
Use a while loop to reverse a given number (e.g., 123 → 321).
'''
#1.Print numbers from 1 to 10 using a while loop.
count=1
while count<=10:
    print(count)
    count+=1    
#2.Write a program that keeps asking the user to enter a password until they
passwd=input("enter the password:")
while passwd!="python123":
    print("wrong password! try again")
    passwd=input("enter the password:") 

#Use a while loop to reverse a given number (e.g., 123 → 321).
num=int(input("enter the number:"))
reverse=0   
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("reversed number:", reverse)  

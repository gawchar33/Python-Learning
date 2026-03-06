sent=input("enter the string")
reverse=sent[::-1]#string slicing it will reverse string like parameters start stop and step so start stop =0 nd step is -1 
if (sent==reverse):
    print("Palindrome")
else:
    print("not palindrome")
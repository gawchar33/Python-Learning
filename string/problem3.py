'''3. String Methods and Functions
1.Take the string "  i love python programming  " and:

2.Remove extra spaces from both ends
3.convert it to title case
4.Count how many times "o" appears
5.Check if the string "123abc" is alphanumeric'''

text="  i love python programming  "#string are immutable in python but we can perform operations on them that will create new strings in memory and assign them to the variable text so the id of text will change because it is now pointing to a new string in memory
print(id(text))
print(f"original string: '{text}'")
#1.Remove extra spaces from both ends
text=text.strip()#python has created a new string with the extra spaces removed and assigned it to the variable text so the id of text will change because it is now pointing to a new string in memory
print(id(text)) #the id of text will change because it is now pointing to a new string in memory
print(f"after removing extra spaces: {text}")


#2.convert it to title case
text=text.title()#python has created a new string with the title case and assigned it to the variable text so the id of text will change because it is now pointing to a new string in memory
print(id(text)) #the id of text will change because it is now pointing to a new string in memory
print(f"after converting to title case: {text}")       
text=text.upper()#python has created a new string with the upper case and assigned it to the variable text so the id of text will change because it is now pointing to a new string in memory
print(id(text)) #the id of text will change because it is now pointing to a new string in memory
print(f"after converting to upper case: {text}")    
text=text.lower()#python has created a new string with the lower case and assigned it to the variable text so the id of text will change because it is now pointing to a new string in memory
print(id(text)) #the id of text will change because it is now pointing to a new string in memory            
print(f"after converting to lower case: {text}")
text=text.capitalize()#python has created a new string with the capitalized case and assigned it to the variable text so the id of text will change because it is now pointing to a new string in memory
print(id(text)) #the id of text will change because it is now pointing to a new string in memory
print(f"after converting to capitalized case: {text}")      


#3.Count how many times "o" appears
text=text.count("o")
print(f"number of times 'o' appears: {text}")

#4.Check if the string "123abc" is alphanumeric
text = "Python123"

print("isalpha:", text.isalpha())#isalpha() method check whether all characters in string is alphabetic or not 
print("isdigit:", text.isdigit())#isdigit() method check whether all characters in string is digit or not
print("isalnum:", text.isalnum())#isalnum() method check whether all characters in string is alphanumeric or not
print("islower:", text.islower())#islower() method check whether all characters in string is lowercase or not
print("isupper:", text.isupper())#isupper() method check whether all characters in string is uppercase or not


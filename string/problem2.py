text="python programming"
print(f"first 6 characters: {text[0:6]}")
print(f"characters 7-19: {text[7:19]}")
print(f"every second character: {text[0:len(text):2]}")
3#reverse the string using slicing it work like start stop and step so we can use negative step to reverse the string
reverse=text[::-1]
print(f"reversed string: {reverse}")
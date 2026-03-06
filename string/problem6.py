'''5. String Manipulation Challenges
1. Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
2. Find the index of the word "Python" in sentence.
3. Convert the entire sentence to uppercase and print it.'''
#1. Given sentence = "Coding in Python is fun", replace "fun" with "awesome" and print it.
sentence="coding in python is fun"
sentence=sentence.replace("fun","awesome")
print(sentence)

#2. Find the index of the word "Python" in sentence.
index=sentence.find("python")
print(f"index of python: {index}")

#3. Convert the entire sentence to uppercase and print it.
sentence=sentence.upper()
print(sentence)

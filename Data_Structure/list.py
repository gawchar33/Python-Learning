numbers=[4,5,9,2]
mixed=["hello",9,8.14]
print(numbers.append(10)) # insert the element at the end of list 
print(numbers)
numbers.insert(2,11) # it will insert the element at the 2nd index in the list
print(numbers)
numbers.remove(2) #  it will remove the number 2 from the list 
print(numbers)
numbers.pop() # it will remove the last element in the list
print(numbers)
numbers.reverse() # it will reverse the list 
print(numbers)
numbers.sort() # it will sort the list in the incremental order
print(numbers)
print(numbers)

# advance use of the list
squared = [x**2 for x in range(5)]
print("square list",squared)  # Output: [0, 1, 4, 9, 16]

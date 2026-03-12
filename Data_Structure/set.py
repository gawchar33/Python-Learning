fruits={"apple","mango","lemon"}
num={1,2,3}
num.add(6) # this will add the element at the end of the set
print(num)
num.remove(2) # it will remove the 2 from set
print(num)
num.discard(4) # it will not give error if the number is not present in the set
print(num)
num.pop() # it will delete the random element from the set 
print(num)

a={1,2,3}
b={3,2,6,4}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
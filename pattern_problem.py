'''Print the following pattern using a for loop:
*
**
***
**** '''
# pythonic way to print the pattern
for i in range(1,5):
    print(f"{'*'*i}")

#another classic way to print the star pattenr in python 
for a in range(1,5):
    for j in range(a):
        print("*",end="")
    print("")
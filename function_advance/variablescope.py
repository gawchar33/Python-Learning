x = 10  # Global variable

def my_func():
    x = 5  # Local variable
    print(x)  # Output: 5

my_func()
print(x)  # Output: 10 (global x remains unchanged)
# global keyword is used to change the variable 
# you can modify global varialbe in function but there scope is only in functiion not outside it but with global you can change it other things 
x = 10  # Global variable

def modify_global():
    global x
    x = 5  # Modifies the global x

modify_global()
print(x)  # Output: 5
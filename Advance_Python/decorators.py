def decorator(func):
    def wrapper():
        print("i am about to execute the function...")
        func()
        print(" function executed")
    return wrapper

1
@decorator # advance way to work with decorators 
def say_hello():
    print("hello")

say_hello()
'''
f will look something like this 
def f():
    print("I am about to execute a function...")
    print("hello !)
    print("i have executed this function....")
    '''

#f=decorator(say_hello)
#f()

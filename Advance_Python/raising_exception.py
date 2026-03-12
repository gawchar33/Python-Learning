age=-10
if age<0:
    raise ValueError("age cannot be negative:")


ages=1

try:
    if age<0:
        print("not good man:")

except KeyError as e:
    print("Error occured:",e)

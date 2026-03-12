x=4
try:
   x=10/0 
except:
   print("value can't be divided by 0")


try:
   x=int("hello")
except TypeError:
   print("type is different:")
except ValueError:
   print("invalid value:")


try:
   x=25/2

except ZeroDivisionError as  e:
   print("error:",e)
   
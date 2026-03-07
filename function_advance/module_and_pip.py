# python have 3 types of modules 1.built-in module , 2.user-defined module, and  third-part modules 
#1. built-in module
import math
print(math.sqrt(9))
#2.user-defined module
import greeting
greeting.greet()

#third-party module 

import requests

response = requests.get("https://api.github.com")

print(response.status_code)
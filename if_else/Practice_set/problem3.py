day=int(input("enter the day number of week:"))
match day:
    case 1:
        print("monday") 
    case 2:
        print("tuesday")    
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")     
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid day number")


        
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
operator=input("enter the operator:" )
match operator:
    case "+":
        print(f"addition of {num1} and {num2} is {num1 + num2}")
    case "-":
        print(f"subtraction of {num1} and {num2} is {num1 - num2}")
    case "*":
        print(f"multiplication of {num1} and {num2} is {num1 * num2}")
    case "/":
        print(f"division of {num1} and {num2} is {num1 / num2}")
    case _:
        print("invalid operator")
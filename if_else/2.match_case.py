status=(input("enter the status code :"))
match status:
    case "200":
        print("ok")
    case "404":
        print("not found")
    case "500":
        print("internal server error")  


'''status=int(input("enter the status code :"))
match status:
    case 200:
        print("ok")
    case 404:
        print("not found")
    case 500:
        print("internal server error")  '''
    
try:
    f=open("data.txt","rt")
    content=f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("file is not here bro ")

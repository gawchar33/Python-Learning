try:
    f=open("data.txt")
except FileNotFoundError:
    print("File not found:")
finally:
    print("operation successfully executed:")
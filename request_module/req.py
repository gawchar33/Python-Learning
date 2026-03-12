import requests

r=requests.get("https://api.github.com/users/gawchar33")


with open("govindgit.txt","w") as f:
    f.write(r.text)
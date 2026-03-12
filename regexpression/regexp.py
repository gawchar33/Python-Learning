import re
text="govind is here and he is enjoying here"
match=re.search("here",text)
print(match)
if match:
    print("match found")
    print("starting index is",match.start())
    print("ending index",match.end())
    
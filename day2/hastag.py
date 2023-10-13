import re
hash=input("Enter the comment: ")
pattern=re.compile("^\#\w*")
h=pattern.findall(hash)
if h:
    print("comments are: "+h[0])
else:
    print("No hastag comments!")
    
    
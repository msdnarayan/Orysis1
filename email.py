import re
mail=input("Enter the mail: ")
pattern=re.compile("^[a-z][a-z 0-9]*@(?!hotmail|yahoo)[a-z]+.(?:com|org|in)")
x=pattern.findall(mail)
if not x:
    print("Not valid")
else:
    print("Valid mail")


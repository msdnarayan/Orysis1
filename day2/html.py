import re
html=input("Enter the text with html tags:")
pattern=re.compile("(?:<[a-z 0-9]+>)+([a-z 0-9 A-Z .]*)")
x=pattern.findall(html)
if x:
    print("Html tags are: ",x)
else:
    print("There are no html tags")
        
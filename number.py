import re
text=input("Enter text:")
pattern=re.compile("\d+")
x=pattern.findall(text)
if x:
    print("Numbers found:",x)
        

    

import re
def valid():
        
    number=input("Enter the phone number: ")
    pattern=re.compile(r"\b\d{10}\b|\b[+]\d{1,3}\s\d{10}\b")
    match=pattern.findall(number)

    if not match:
        print("Not valid phone number")

    else:
        print("Valid phone number")
        
valid()



    
    
import re
ip=input("Enter the IPv4 address:")
pattern=re.compile("^\d{3}.\d{3}.\d{1}.\d{1}")
x=pattern.findall(ip)
if x:
    print("IP is valid",x[0])
else:
    print("Not avlid IPv4 address! ")
        
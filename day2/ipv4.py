import re
ip=input("Enter the IPv4 address:")
pattern=re.compile("(?:[0][0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]).(?:[0][0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]).(?:[0][0-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])")
x=pattern.findall(ip)
if x:
    print("IP is valid",x[0])
else:
    print("Not avlid IPv4 address! ")
        
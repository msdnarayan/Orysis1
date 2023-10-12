import re
def date(y):
    pattern=re.compile("\d{1,12}[\/](?:[0-2][0-9]|[3][0-1])[\/](?!0000)\d{4}")
    dat=pattern.findall(y)
    if not dat:
        print("Not valid format(MM/DD/YYYY)!")
    else:
        print("valid: "+dat[0])
def main():
    d=input("Enter the date (MM/DD/YYYY): ")
    date(d)
    
main()
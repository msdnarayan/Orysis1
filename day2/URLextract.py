
import re
url=input("Enter the input: ")
pattern=re.compile("(?:http:\/\/www.)|(?:www.)(?:[a-z . 0-9]*[a-z . 0-9]+.(?:com|in|org))")
ur=pattern.findall(url)
if ur:
    print("The URL is:",ur[0])
else:
    print("No URL found")
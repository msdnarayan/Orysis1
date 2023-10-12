

word=input("Enter the word: ");
##c=cc=0
ac=ec=ic=oc=uc=ccount=0
for i in word:
    if i == 'a' or i=='A':
        ac+=1;
    elif i == 'e' or i=='E':
        ec+=1;
        
    elif i == 'i' or i=='I':
        ic+=1;
       
    elif i == 'o' or i=='O':
        oc+=1;
        
    elif i == 'u' or i=='U':
        uc+=1;
        
    else:
        ccount+=1;
        

 #   if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
 #       c+=1
  #  else:
 #       cc+=1
 
 
print("Total number of vowels: \n")
print("a: ",ac)
print("e: ",ec)
print("i: ",ic)
print("o: ",oc)
print("u: ",uc)
print("Total number of consonants: ",ccount)

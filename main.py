n=4
strr=''
for i in range(n):
 
 for j in range(n-i-1):
   strr=strr+"5"
 for k in range(i+1):
   strr=strr+"#"
 strr= strr+"\n"
print(strr)
M=int(input())
lis=[]
n=0
sen=input()    
a=sen.split(" ")
a1=[]
for x in a:
    x=x.strip(".-?!',")
    x=x.lower()
    if len(x)>0:
        a1.append(x)
for x in a1:
    if x not in lis:
        n+=1 
        if len(lis)>=M:
            lis.pop(0)
        lis.append(x)
n1=len(a1)
print(n1)
print(n)
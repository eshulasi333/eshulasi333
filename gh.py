import math
def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    q=int(math.sqrt(n))+1
    for er in range(3,q):
        if n%er==0:
            return False
    else:
        return True
mi=[]
ad=[]
num=[]
for x in range(2,1000001):
    if prime(x):
        mi.append(x)
for r in range(len(mi)):
    su=mi[r]
    i=0
    for fr in range(r+1,len(mi)):
        tr=su+mi[fr]
        su+=mi[fr]
        i+=1
        if tr in mi:
            ad.append(i)
            num.append(su)
        if su>1000000:
            break
            
val=ad.index(max(ad))
print(num[val])
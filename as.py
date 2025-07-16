import math
def pri(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for x in range(3,int(math.sqrt(n))+1,2):
        if n%x==0:
            return False
    else:
        return True
def ty():
    li=[]
    for x in range(100):
        for y in range(100):
            z=x**y
            sum=0
            for e in str(z):
                sum+=int(e)
            li.append(sum)
    print(max(li))
i=1
while True:
    i+=2
    if not pri(i):
        for x in range(1,int(math.sqrt(i))+1):
            a=i-2*x**2
            if pri(a):
                break
        
        else:
            print(i)
            break
        
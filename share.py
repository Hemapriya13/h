T=int(input("enter Number of test cases:"))
case=[]
for i in range(0,T):
    size=[]
    N=int(input("No of doges"))
    for j in range(0,N):
        s=int(input("size of a dog"))
        size.append(s)
    s1=sorted(size)
    s2=[]
    c=[]
    share=0
    for e in s1:
        if e not in s2:
            s2.append(e)
    for e1 in range(0,len(s2)):
        c1=s1.count(s2[e1])
        c.append(c1)
    l=len(c)
    for e2 in range(0,l):
        share+=(c[e2]*(e2+1))
    case.append(share)
for i in range(0,len(case)):
    print("case#%d:%d" %(i+1,case[i]))

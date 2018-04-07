n = int(input())
ans=0
def BruteForce(i,s):
    x = [int(x) for  x in str(s)]
    if sorted(x) == x:
        return s

    else:
        return BruteForce(i,s-1)


def logic(i,s):
    temp=s

    for i in range(len(s),1,-1):
        x=i-1

        if s[x-2]>=s[x-1]:
            if i>-1:
                if s[x-1]==0 and s[x]==0:
                    s[x-1]=9
                    s[x]=9
                    if (s[x-2]-1)<0:
                        s[x-2]==0
                    else:
                        s[x-2]-=1
                while s[x-1]>s[x]:
                    aj=s[x-1]
                    ai=s[x]

                    ai+=9
                    if ai>=10:
                        ai-=10
                    aj-=1
                    if aj<0:
                        aj+=10
                    s[x-1]=aj
                    s[x]=ai
                if s[x-1]==s[x]:
                    pass
        else:
            x1=int(str(s[x-1])+str(s[x]))
            x1=str(BruteForce(i,x1))
            s[x-1]=int(x1[0])
            s[x]=int(x1[1])
    # return logic(i,s)
    if s[-1]<9:
        s[-1]=9
    return s


def ordertest(i,s):
    x = [int(x) for  x in str(s)]
    if sorted(x) == x:
        print("Case #{0}: {1}".format(i, s))
    else:
        ordertest(i,s-1)

for i in range(n):
    s=input()
    temp=int(s)
    s=[int(x) for x in list(s)]
    # if s[-1]==0 and s[-2]==0:


    if len(s)>2:
        res=logic(i+1,s)
        r1=""
        if res[0]==0:
            del res[0]

        aahaa=True
        while aahaa:
            res=logic(i+1,res)
            if res.index(min(res))==0:
                aahaa=False
                break

        for x in res:
            r1+=str(x)
        print("Case #{0}: {1}".format(i+1, r1))
    elif len(s)==2:
        res=ordertest(i+1,temp)
    elif len(s)==1:
        print("Case #{0}: {1}".format(i+1, s[0]))

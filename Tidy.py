n = int(input())
ans=0
def BruteForce(i,s):
    x = [int(x) for  x in str(s)]
    # print('Entering X' )
    # print(x)

    if sorted(x) == x:
        return s

    else:
        return BruteForce(i,s-1)

    # print(s)


def logic(i,s):
    temp=s

    for i in range(len(s),1,-1):
        print(s)
        print(i)
        x=i-1
        if s[x-2]>=s[x-1]:
            print(s[x-1],s[x-1])
            if i>-1:
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
    return logic(i,s)

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


    if len(s)>2:
        res=logic(i+1,s)
        print("Final Result is")
        print(res)
    elif len(s)==2:
        res=ordertest(i+1,temp)
    elif len(s)==1:
        print(s[0])

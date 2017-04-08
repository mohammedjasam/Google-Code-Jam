n = int(input())
ans=0
def BruteForce(i,s):
    try:
        x = [int(x) for  x in str(s)]
        print('Entering X' )
        print(x)

        if sorted(x) == x:
            print(x)
        else:
            BruteForce(i,s-1)

    except:
        return s


def logic(i,s):
    temp=s

    for i in range(len(s),1,-1):
        # print(i,s[i-1])

        print(i)
        x=i-1
        if s[x-2]>=s[x-1]:
            if i>-1:
                # print(s[x],s[x-1])
                while s[x-1]>=s[x]:
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
                    print(s)
                print("yes")
                print(s[x-1],s[x])
        else:
            x1=int(str(s[x-1])+str(s[x]))
            print('x1 is ')
            print(x1)
            try:
                x1=str(BruteForce(i,x1))
            except:
                x1=ans
            print('x1 after bf '+str(x1))
            s[x-1]=int(x1[0])
            s[x]=int(x1[1])
        #     else:
    #         string=""
    #         string+=str(s[i-2]) + str(s[i-1])+str(s[i])
    #         print(string)
    #         string=str(BruteForce(i,int(string)))
    #         string=list(string)
    #         string=reversed(string)
    #         print(string)
    #         s[i],s[i-1],s[i-2]=string[0],string[1],string[2]
    # print(s)

    # if sorted(x) == x:
    #     print("Case #{0}: {1}".format(i, s))

    # else:
    #     check(i,s-1)
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
    elif len(s)==2:
        res=ordertest(i+1,temp)
    elif len(s)==1:
        print(s[0])

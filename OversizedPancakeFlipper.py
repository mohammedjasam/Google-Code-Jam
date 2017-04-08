import sys
n = int(input())

for i in range(n):
    d={}
    s,k=input().split()
    s=list(s)
    for j in range(len(s)):
        d[j]=s[j]
    # print(d)
    c=0
    for j in range(len(d)):
        # d[j]=s[j]
        if d[j]!='-':
            pass
        else:
            for x in range(int(k)):
                # print(x)
                try:
                    if d[j+x]=='+':
                        d[j+x]='-'
                        # c+=1
                    else:
                        d[j+x]='+'
                except:
                    print('IMPOSSIBLE')
                    sys.exit()
            c+=1
                # print(d)
    print(c)

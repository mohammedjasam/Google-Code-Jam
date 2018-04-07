#
# # TIDY Brute FORCE:
#
# n = int(input())
#
# def ordertest(i,s):
#     x = [int(x) for  x in str(s)]
#     if sorted(x) == x:
#         print("Case #{0}: {1}".format(i, s))
#     else:
#         ordertest(i,s-1)
#

###### Very easy! Couldn't qualify though! Anyway, there's always a next time ;)
n=int(input())
for i in range(n):
    temp=[int(x) for x in list(input())]
    for j in range(len(temp)-1,0,-1):
        if temp[j]<temp[j-1]:
            temp[j-1]-=1
            for x in  range(j,len(temp)):
                temp[x]=9
    res=""
    for x in temp:
        res+=str(x)
    print("Case #{0}: {1}".format(i+1, int(res)))

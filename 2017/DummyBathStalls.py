n = int(input())

import math
def checkLeft(l,s):
    c=0
    length=len(l)
    for i in range(s-1, -1, -1):

        if l[i]!=1:
            c+=1
        else:
            break
    return c
def checkRight(l,s):
    c=0
    length=len(l)
    for i in range(s+1, length):
        if l[i]!=1:
            c+=1
        else:
            break
    return c
#####################################

for i in range(n):
    n, k = map(int, input().split())
    l1={}
    l1[0]=1
    for j in range(1,n+1):
        l1[j]=0
    l1[n+1]=1
    l2={}
    l2[0]=(-1,-1)
    for j in range(1,n+1):
        l2[j]=(-1,-1)
    l2[n+1]=(-1,-1)

    # print("Initial l1 & l2")
    # print(l1)
    # print(l2)
    # print()
    if k==n:
        finalmax=0
        finalmin=0
        print("Case #{0}: {1} {2}".format(i+1,finalmax, finalmin))
    elif math.ceil(n/2)==k:
        print("Case #{0}: {1} {2}".format(i+1,math.ceil(n/2),math.ceil(n/2)-1))
    else:
        for abc in range(k):
            # print()
            # print("Iteration #" +str(abc+1))

             ########## Created the toilet room
            # print(l1)
            minarr={}
            maxarr={}
            minarr[0]=-1
            maxarr[0]=-1
        # for i in range(len(l1)):
        #     print(l1[i])
        #     print(l2[i])
            for ax in range(1,len(l1)-1): ######## Verified and calculated left and right

                if l1[ax]==1:
                    l2[ax]=((-1,-1))
                    minarr[ax]=(-1)
                    maxarr[ax]=(-1)
                    pass

                else:
                    left=checkLeft(l1,ax)
                    right=checkRight(l1,ax)
                    l2[ax]=((left,right))
                    # print(minarr)
                    minarr[ax]=(min(left,right))

                    maxarr[ax]=(max(left,right))
            # print('minarr is')
            # print(minarr)
            # print('maxarr is')
            # print(maxarr)
            # print("l1 and l2 is:")
            # print(l1)
            # print(l2)
            # print("Minarr is:")
            # print(minarr)


            maxsubarr={}

            # finds out the max in minarry and found indices!
            for aj in range(1, len(minarr)):
                maxi=max(minarr.values())
                temp=minarr[aj]
                # print(temp)
                # print(maxi)
                ctr=0
                if maxi <= temp:
                    ctr+=1
                    maxi=temp
                    maxsubarr[ctr]=aj
            # print(maxsubarr)
            templ={}
            # print("Maxarr is:")
            # print(maxarr)

            # if there are more than one max element in min array!!
            print("len of maxsubarr is : "+str(len(maxsubarr.values())))
            if len(maxsubarr)>1:
                # print("HI")
                print(maxsubarr)
                # if maxarr[maxsubarr[1]]==0:
                #     del maxsubarr[0]

                for x in range(len(maxsubarr.values())):
                    templ[x]=(maxarr[x])
                    # print(maxarr[x])
                counter=0
                maximum=max(templ.values())
                for x in templ:
                    if maximum <= x:
                        counter+=1
                if counter>1:
                    print(l2[maxsubarr[1]])
                    finalmax=max(l2[maxsubarr[1]])
                    finalmin=min(l2[maxsubarr[1]])
                    # print(finalmax,finalmin)
                    l1[maxsubarr[1]]=1
                    l2[maxsubarr[1]]=(-1,-1)
                    minarr[maxsubarr[1]]=-1
            else:
                finalmax=max(l2[maxsubarr[1]])
                finalmin=min(l2[maxsubarr[1]])
                l1[maxsubarr[1]]=1
                minarr[maxsubarr[1]]=-1
                l2[maxsubarr[1]]=1
                lol=1
            #     print(l2)
            #
            # print(maxsubarr)
            # print("Maxarr is:")
            # print(maxarr)
            # print("===================================================")
        # print(finalmax,finalmin)
        print("Case #{0}: {1} {2}".format(i+1,finalmax, finalmin))

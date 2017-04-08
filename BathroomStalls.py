n = int(input())
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
    l1=[]
    l1.append(1)
    for j in range(n):
        l1.append(0)
    l1.append(1)
    l2=[]
    l2.append((-1,-1))
    for j in range(n):
        l2.append((-1,-1))
    l2.append((-1,-1))

    # print("Initial l1 & l2")
    # print(l1)
    # print(l2)
    # print()
    for abc in range(k):
        # print()
        # print("Iteration #" +str(abc+1))

         ########## Created the toilet room
        # print(l1)
        minarr=[]
        maxarr=[]
        minarr.append(-1)
        maxarr.append(-1)
        for ax in range(1,len(l1)-1): ######## Verified and calculated left and right

            if l1[ax]==1:
                l2[ax]=((-1,-1))
                minarr.append(-1)
                maxarr.append(-1)
                pass

            else:
                left=checkLeft(l1,ax)
                right=checkRight(l1,ax)
                l2[ax]=((left,right))
                # print(minarr)
                minarr.append(min(left,right))
                maxarr.append(max(left,right))
        # print("l1 and l2 is:")
        # print(l1)
        # print(l2)
        # print("Minarr is:")
        # print(minarr)


        maxsubarr=[]

        # finds out the max in minarry and found indices!
        for aj in range(1, len(minarr)):
            maxi=max(minarr)
            temp=minarr[aj]
            if maxi <= temp:
                maxi=temp
                maxsubarr.append(aj)
        templ=[]
        # print("Maxarr is:")
        # print(maxarr)

        # if there are more than one max element in min array!!
        if len(maxsubarr)>1:
            if maxarr[maxsubarr[0]]==0:
                del maxsubarr[0]
            for x in maxsubarr:
                templ.append(maxarr[x])
                # print(maxarr[x])
            counter=0
            maximum=max(templ)
            for x in templ:

                if maximum <= x:
                    counter+=1
            if counter>1:
                finalmax=max(l2[maxsubarr[0]])
                finalmin=min(l2[maxsubarr[0]])
                l1[maxsubarr[0]]=1
                l2[maxsubarr[0]]=(-1,-1)
                minarr[maxsubarr[0]]=-1
        else:
            finalmax=max(l2[maxsubarr[0]])
            finalmin=min(l2[maxsubarr[0]])
            l1[maxsubarr[0]]=1
            minarr[maxsubarr[0]]=-1
            l2[maxsubarr[0]]=1
        # print(maxsubarr)
        # print("Maxarr is:")
        # print(maxarr)
        # print("===================================================")

    print(finalmax,finalmin)

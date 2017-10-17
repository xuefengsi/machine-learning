#from collections import deque
'''def Reverse(lists):
    ReverseList = []
    for i in range(0,len(lists)):
        ReverseList.append(lists[len(lists)-i-1])
    return ReverseList'''
'''
def OperationList(lists,n):
    returnList = []
    for i in range(0,n):
        returnList.append(lists[i])
        #returnList = Reverse(returnList)
        returnList.reverse()
    returnList = ''.join(f+' ' for f in returnList)
    print(returnList.strip())


if __name__ == '__main__':
    OperatedNum = int(input())
    lists = input().split(" ")
    OperationList(lists,OperatedNum)'''

def AL(list):
    Alen = len(list)
    B = []
    result = []
    for i in range(0,Alen):
        if(list[i]>0):
            B.append(i)
    for i in range(0,len(B)):
        for g in range(i+1,len(B)):
            sum = 0
            for j in range(B[i],B[g]+1):
                sum += list[j]
            result.append(sum)
    Amax = max(result)
    return Amax
if __name__ == '__main__':
    list=input().split(" ")
    A=len(list)
    B = []
    d = 0
    for i in range(0,A):
        mid = int(list[i])
        B.append(mid)
    for i in range(0,len(B)):
        if(B[i]<=0):
            d += 1
    if d == len(B) or d == len(B)-1:
        print(max(B))
    else:
        print(AL(B))




def AL(list):
    Alen = len(list)
    B = []
    result = []
    for i in range(0,Alen):
        if(list[i]>0):
            B.append(i)
    for i in range(0,len(B)):
        for g in range(i+1,len(B)):
            sum = 0
            for j in range(B[i],B[g]+1):
                sum += list[j]
            result.append(sum)
    Amax = max(result)
    return Amax
if __name__ == '__main__':
    list=input().split(" ")
    A=len(list)
    B = []
    d = 0
    for i in range(0,A):
        mid = int(list[i])
        B.append(mid)
    for i in range(0,len(B)):
        if(B[i]<=0):
            d += 1
    if d == len(B) or d == len(B)-1:
        print(max(B))
    else:
        print(AL(B))
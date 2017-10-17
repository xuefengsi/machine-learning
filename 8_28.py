'''def MaxValue(list):
    llen = []
    result = []
    B = list[0]
    for i in range(0,len(list)):
        llen.append(len(list[i]))
    MoveLen = llen[0]
    for i in range(1,len(list)):
        B = B + list[i]
    for i in range(1,len(llen)):
        result.append(rotateString(B,MoveLen))
        MoveLen = MoveLen + llen[i]
    return result

def rotateString(A,p):
    A = list(A)
    A.reverse()
    B = A[:len(A) - p ]
    C = A[len(A) - p:]
    B.reverse()
    C.reverse()
    result = B + C
    print(B+C)


if __name__ == '__main__':
    Alen = int(input())
    B = input().split(" ")
    print(len(B))
    print(MaxValue(B))
    #print(list)
'''
def insert_sort(list):
    count = len(list)
    for i in range(0,count):
        j=i-1
        key=list[i]
        while j>=0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1
    return list

def shell_sort(list):
    count = len(list)
    step = 2
    group = int(count/step)
    while group>0:
        for i in range(0,group):
            j = i + group
            while j<count:
                k = j - group
                key = list[j]
                while k>=0:
                    if list[k] > key:
                        list[k+group] = list[k]
                        list[k] = key
                    k -= group
                j += group
        group = int(group/step)
    return list
def bubble_sort(list):
    count = len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if list[i] > list[j]:
                list[i],list[j]=list[j],list[i]
    return list
def select_sort(list):
    count = len(list)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if list[min] > list[j]:
                min = j
            list[min],list[i]=list[i],list[min]
    return list

def quick_sort(list,left,right):
    if left >= right:
        return list
    low = left
    high = right
    key = list[left]
    while left<right:
        while left<right and list[right]>=key:
            right -= 1
        list[left] = list[right]
        while left<right and list[left]<=key:
            left += 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list,low,left-1)
    quick_sort(list,left+1,high)
    return list

def merge_sort(list):
    if len(list)<=1:
        return list
    mid = int(len(list)/2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)
def merge(left,right):
    result = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
if __name__ == '__main__':
    a = input().split()
    #print(insert_sort(a))
    #print(shell_sort(a))
    #print(bubble_sort(a))
    #print(select_sort(a))
    #print(quick_sort(a,0,len(a)-1))
    print(merge_sort(a))

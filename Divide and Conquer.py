'''import math
from numpy import *
def BinarySearch(T,x):
    l = 1; r = len(T)
    while l<= r:
        m = math.floor((l + r)/2)
        if T[m] == x:
            return m
        elif T[m] > x:
            r = m-1
        else:
            l = m+1
    return 0

##插入排序
def insert_sort(lists):
    count = len(lists)
    for i in range(1,count):
        key = lists[i]
        j = i-1
        while j >=0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

##希尔排序




##冒泡排序
def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists


##快速排序
def quick_sort(lists,left,right):
    if left >=right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left<right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left<right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists

##直接选择排序
def select_sort(lists):
    count = len(lists)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if lists[min] > lists[j]:
                min = j
        lists[i],lists[m]=lists[m],lists[i]
    return lists

##归并排序
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists)/2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left,right)

def merge(left,right):
    i,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result'''

###快速排序
def partition(li, start, end):
    li_len = end - start + 1
    if li_len < 2:
        raise ValueError("list which lenght is less then 2 do not need to partition")
    #使用最后一个元素作为分割点
    key = li[end]
    middle_index = start
    for x in range(start, end):
        if li[x] < key:
            li[middle_index], li[x] = li[x], li[middle_index]
            print(li[x])
            print(li[middle_index])
            middle_index += 1
    li[end], li[middle_index] = li[middle_index], li[end]
    return middle_index


def sort(li, start, end):
    li_len = end - start + 1
    if li_len < 2:
        return li
    middle_index = partition(li, start, end)#找到首元素A[p]在排序后的位置
    #print(middle_index)
    #print(',')
    sort(li, start, middle_index - 1)
    sort(li, middle_index + 1, end)
    return li


def main():
    l = [2, 3, 4, 23,45,6,9,12,134,4,6,1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = sort(l, 0, len(l) - 1)
    print (li)


if __name__ == '__main__':
    main()


'''def distance(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist
def perimeter(x1,y1,x2,y2,x3,y3):
    if ((x2-x1) * (y3-y2) - (x3-x2) * (y2-y1)) != 0:
        return (distance(x1,y1,x2,y2) + \
                distance(x2,y2,x3,y3) +\
                distance(x1,y1,x3,y3))

if __name__ == '__main__':
    x1,y1 = input("point1: (x,y)=")
    x2,y2 = input("point2: (x,y)=")
    x3,y3 = input("point3: (x,y)=")
    perimeter(x1,y1,x2,y2,x3,y3)'''


'''##n皇后问题' \
import math
def place(x,k):
    for i in range(0,k):
        if((x[i]==x[k]) or (abs(x[i]-x[k])==abs(i-k))):
            return False
    return True

def n_queen(x,n):
    k=0;x[0]=0;flag=False
    while(k>=0):
        while(x[k]<=n):
            if(not place(x,k)):
                x[k]=x[k]+1
            else:
                if(k==n):
                    print(x)
                    flag=True
                    break
                else:
                    k=k+1;
                    x[k]=0
        if(flag):
            break
        else:
            x[k]=0
            k=k-1
            x[k]=x[k]+1
if __name__ == '__main__':
    x=[0,0,0,0,0]
    n=4
    n_queen(x,n)'''




'''##图的着色问题
import math
import numpy as np

bmap = np.matrix([
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1]
])


def colored(x, k):
    for i in range(0, k):
        if ((x[i] == x[k]) and bmap[k, i]):
            return False
    return True


def map_color(x, n, m):
    k = 0
    x[0] = 0
    flag = False
    while (k >= 0):
        while (x[k] <= m):
            if (not colored(x, k)):
                x[k] = x[k] + 1
            else:
                if (k == n):
                    print  (x)
                    flag = True
                    break
                else:
                    k = k + 1
                    x[k] = 0
        if (flag):
            break
        else:
            x[k] = 0
            k = k - 1
            x[k] = x[k] + 1


if __name__ == '__main__':
    x = [0, 0, 0, 0, 0, 0]
    map_color(x, 5, 3)'''



















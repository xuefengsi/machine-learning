'''import math
def distance(x1,y1,x2,y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist
def perimeter(x1,y1,x2,y2,x3,y3):
    if ((x2-x1) * (y3-y2) - (x3-x2) * (y2-y1)) != 0:
        return (distance(x1,y1,x2,y2) + \
                distance(x2,y2,x3,y3) +\
                distance(x1,y1,x3,y3))

if __name__ == '__main__':
    print(perimeter(1,3,5,7,4,2))'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''def partition(li, start, end):
    li_len = end - start + 1
    if li_len < 2:
        raise ValueError("list which lenght is less then 2 do not need to partition")
    #使用最后一个元素作为分割点
    key = li[end]
    middle_index = start
    for x in range(start, end):
        if li[x] < key:
            li[middle_index], li[x] = li[x], li[middle_index]
            middle_index += 1
    li[end], li[middle_index] = li[middle_index], li[end]
    return middle_index


def sort(li, start, end):
    li_len = end - start + 1
    if li_len < 2:
        return li
    middle_index = partition(li, start, end)
    sort(li, start, middle_index - 1)
    sort(li, middle_index + 1, end)
    return li


def main():
    l = [2, 3, 4, 23,45,6,9,12,134,4,6,1, 7, 3, 8, 1100, 282828, 1, 20, 0]
    li = sort(l, 0, len(l) - 1)
    print (li)


if __name__ == '__main__':
    main()'''

'''import math

##n皇后问题
def place1(x, k):
    for i in range(0, k):
        if ((x[i] == x[k]) or (abs(x[i] - x[k]) == abs(i - k))):
            return False
    return True


def n_queen1(x, n):
    k = 0
    x[0] = 0
    flag = False
    while (k >= 0):
        while (x[k] <= n):
            if (not place1(x, k)):
                x[k] = x[k] + 1
            else:
                if (k == n):
                    print (x)
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


def place(x, k):
    for i in range(1, k):
        if ((x[i] == x[k]) or (abs(x[i] - x[k]) == abs(i - k))):
            return False
    return True


def n_queen(x, n):
    k = 1
    x[1] = 0
    while (k > 0):
        x[k] = x[k] + 1
        while ((x[k] <= n) and (not place(x, k))):
            x[k] = x[k] + 1
        if (x[k] <= n):
            if (k == n):
                print (x[1:n + 1])
                break
            else:
                k = k + 1
                x[k] = 0
        else:
            x[k] = 0
            k = k - 1


if __name__ == '__main__':
    x = [0, 0, 0, 0]
    n_queen1(x, 3)
    # x = [0,0,0,0,0]
    # n_queen(x,4)'''

'''
###地图着色问题
import math
import numpy as np
bmap = np.matrix([
    [1,1,0,1,0],
    [1,1,1,0,1],
    [0,1,1,1,1],
    [1,0,1,1,0],
    [0,1,1,0,1]
])


def colored(x,k):
    for i in range(0,k):
        if((x[i]==x[k]) and bmap[k,i]):
            return False
    return True

def map_color(x,n,m):
    k=0;x[0]=0;flag=False
    while(k>=0):
        while(x[k]<=m):
            if(not colored(x,k)):
                x[k]=x[k]+1
            else:
                if(k==n):
                    return x
                    flag=True
                    break
                else:
                    k=k+1
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
    m=0
    while(m<=n):
        if(map_color(x,n,m)):
            print(map_color(x,n,m))
            print(m)
            break
        else:
            m += 1'''

'''import math

def place(x,k):
    for i in range(0,k):
        if((x[i]==x[k]) or (abs(x[i]-x[k]) == abs(i-k))):
            return False
    return True

def n_queen(x,n):
    k = 0
    x[0] = 0
    flag = False
    while(k>=0):
        while(x[k]<=n):
            if(not place(x,k)):
                x[k] = x[k] + 1
            else:
                if(k==n):
                    print(x)
                    flag = True
                    break
                else:
                    k = k + 1
                    x[k] = 0
        if(flag):
            break
        else:
            x[k] = 0
            k = k-1
            x[k] = x[k] + 1

if __name__ == '__main__':
    x = [0,0,0,0]
    n = 3
    n_queen(x,3)'''


'''
def insert_sort(lists):
    count = len(lists)
    for i in range(0,count):
        key = lists[i]
        j = i - 1
        while(j>=0):
            if(lists[i]<lists[j]):
                lists[i] = lists[j]
                lists[j] = key
            j -= 1
    return lists
if __name__ == '__main__':
    a = [3,1,2,5]
    print(insert_sort(a))'''



'''def shell_sort(lists):
    count = len(lists)
    step = 2
    group = int(count/step)
    while group > 0:
        for i in range(0,group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
            j += group
        group = int(group/step)
    return  lists'''
'''def shell_sort(lists):
    count = len(lists)
    step = 2
    group =int(count / step)
    while group > 0:
        for i in range(0,group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k>=0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group =int(group/step)
    return lists

if __name__ == '__main__':
    a = [3,1,2,4,6]
    print(shell_sort(a))'''
from collections import deque
'''def A(number,cnt):
    count = len(number)
    k = 0
    i = count -1
    # print(cmin)
    while i >= 0 and cnt > 0:
        cmin = min(number)
        # print(len(number))
        if number[i] == cmin:
            del (number[i])
            i = len(number) - 1
            cnt -= 1
        else:
            i -= 1
    number = ''.join(f + '' for f in number)
    #print(number)
    number = int(number)
    return number



if __name__ == '__main__':
    a = []
    number = list(input())
    b = int(input())
    A(number,b)'''
'''from collections import deque
def NC(n,number):
    a = []
    b = []
    for i in range(0, len(number)):
        a.append(list(number[i]))
    while n>0:
        amax = max(a[i][0] for i in range(0,n))
        for i in range(0,n):
            if a[i][0] == amax:
                b.append(number[i])
                del(a[i])
                print(a)
                n -= 1
    b = ''.join(f+'' for f in b)
    print(b)

if __name__ == '__main__':
    n = int(input())
    number =input().split(" ")
    NC(n,number)
'''
'''def compared(a,b):
    count = len(a)
    k = 0
    a=list(a)
    b=list(b)
    for i in range(0,count):
        if a[i]!=b[i]:
            k += 1
    return k
def A(lists,B):
    m = 0
    count = len(lists)
    for i in range(0,count):
        h = compared(lists[i], B)
        if h==1:
                print(m)
                return m
                m += len(lists)+1
        else:
            m += len(lists)+1


if __name__ == '__main__':
    T=int(input())
    a = []
    for i in range(0,T):
        lists = input().split(" ")
        # lists = lists.split(" ")
        B = lists[1]
        lists = lists[0].split("_")
        a.append(A(lists, B))
    for i in range(0,T):
        print(a[i])'''
'''
def insert_sort(lists):
    count = len(lists)
    for i in range(0,count):
        j = i -1
        key = lists[i]
        while j>=0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
    #时间复杂度为平均O（n**2)，最好o(n),最坏o(n**2) 空间复杂度o(1) 稳定

'''
'''
def shell_sort(lists):
    count = len(lists)
    step = 2
    group = int(count/step)
    while group>0:
        for i in range(0,count):
            j = i + group
            while j<count:
                key = lists[j]
                k = j - group
                while k>=0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group = int(group/step)
    return lists
    #希尔排序平均时间复杂度为o(n**3/2),最好为o(n),最坏为o(n**2)，空间复杂度为o(1),稳定
'''
'''
def select_sort(lists):
    count = len(lists)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if lists[j]<lists[min] :
                lists[j],lists[min]=lists[min],lists[j]

    return lists
    #直接选择排序平均时间负责度为o(n**2),最好，最坏都为o(n**2），空间复杂度o(1),不稳定
'''
'''
def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists
    #冒泡排序,平均时间复杂度为o(n**2),最好为o(n),最坏为o(n**2),空间复杂度为o(1),稳定
'''
'''
def quick_sort(lists,left,right):
    if left > right:
        return lists
    low = left
    high = right
    key = lists[left]
    while left < right:
        while left<right and lists[right]>=key:
            right -= 1
        lists[left]=lists[right]
        while left<right and lists[left]<=key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists
    #快速排序的平均时间复杂度为o(nlogn)，最好o(nlogn),最坏o(n**2),空间复杂度o(logn),不稳
'''
'''
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    mid = int(len(lists)/2)
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left,right)
def merge(left,right):
    i,j=0,0
    result = []
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
    #归并排序的平均时间复杂度为o(nlogn),最好最坏都为o(nlogn)空间复杂度为o(n)，稳定
'''

'''if __name__ == '__main__':
    a = [1,3,2,4]
    #print(insert_sort(a))
    #print(shell_sort(a))
    #print(select_sort(a))
    #print(bubble_sort(a))
    #print(quick_sort(a,0,3))
    print(merge_sort(a))
    '''


'''
x = input()
y = input()
t = 0
flag = 1
for j in y:
    if x.find(j,t)==-1:
        flag=0
        break
    else:
        t=x.find(j,t)+1
if flag==1:
    print('Yes')
else:
    print('No')
'''
'''
if __name__ == '__main__':
    try:
        while 1:
            s = input()
            out = int(s, 16)
            print(out)
    except:
        pass
'''
'''
if __name__ == '__main__':
    while 1:
        try:
            num = input().split(" ")
            s = 0
            for i in range(0,6):
                if int(num[i]) < int(num[0]):
                    s += int(num[i])
            print(s)
        except:
            break

'''
'''
if __name__ == '__main__':
    while 1:
        try:
            num = input().split(" ")
            num[0] = int(num[0])
            num[1] = int(num[1])
            if num[0]==num[1]==0:
                for i in range(0,len(result)):
                    print(result[i])
                break
            else:

                s = 1
                while(num[1] >= 2*num[0]):
                    if num[1]==2*num[0]:
                        s += 1
                        num[1] -= 2*num[0]
                    else:
                        s += 2
                        num[1] -= 2 * num[0]
                result.append(s)
        except:
            break


'''
'''
from collections import  deque
def place(x,k):
    for i in range(0,k):
        if x[i]==x[k] or abs(x[i]-x[k])==abs(i-k):
            return False
    return True

def n_queen(x,n):
    k=0
    x[0]=0
    result = []
    flag=False
    while k>=0:
        while x[k]<=n:
            if(not place(x,k)):
                x[k] = x[k] + 1
            else:
                if k==n:
                    #x = ''.join(f+'' for f in x)
                    x=[str(i) for i in x]
                    x=''.join(f+'' for f in x)
                    result.append(int(x))
                    flag = True
                    break
                else:
                    k=k+1
                    x[k]=0
        if(flag):
            

        else:
            x[k]=0
            k=k-1
            x[k]=x[k]+1
    return sorted(result)
if __name__ == '__main__':
    x=[0,0,0,0,0,0,0,0]
    a = n_queen(x,7)
    print(a)
    result = []
    n = int(input())
    for i in range(0,n):
        b = int(input())
        result.append(a[b-1])
    for i in range(0,n):
        print(result[i])
'''
'''
#明文加密
if __name__ == '__main__':
    try:
        while 1:
            start = input()
            if start=="ENDOFINPUT":
                break
            secret = input()
            end = input()
            secret_Text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            plain_Text = 'VWXYZABCDEFGHIJKLMNOPQRSTU'
            plain = ''
            for c in secret:
                if c in secret_Text:
                    plain = plain + plain_Text[secret_Text.index(c)]
                else:
                    plain = plain + c
            print(plain)
    except:
        pass
'''
'''
from collections import deque
def quick_sort(list,left,right):
    if left>=right:
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
'''
'''
def merge_sort(list):
    if len(list)<=1:
        return list
    mid = int(len(list)/2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)
def merge(left,right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
'''
def select_sort(list):
    count = len(list)
    for i in range(0,count):
        m = i
        for j in range(i+1,count):
            if list[j] < list[m]:
                m = j
        list[i],list[m]=list[m],list[i]
    return list
if __name__ == '__main__':
    list = input().split(" ")
    #result = merge_sort(list)
    result = select_sort(list)
    result = ''.join(f + ' ' for f in result)
    print(result)









































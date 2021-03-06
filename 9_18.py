'''
import random
import os
os.chdir('C:\\Users\\sixuefeng\\Desktop\\学习\\中科院')
def createdata():
   point = []
   for i in range(0,128*128*128*3):
        point.append(random.randint(0,1000))
   return point
def WriteToTxt(list_name,file_path):
    fp = open(file_path,"w+")
    len = 0
    i = 1
    for item in list_name:
        len += 1
        if (len-1) % 3 == 0:
            fp.write(str(i) + '\t' + str(item) + '\t')
            i += 1
        elif len % 3== 0 and len <128*128*128*3:
            fp.write(str(item) + '\n')
        else:
            fp.write(str(item) + '\t')
    fp.close()
if __name__ == '__main__':
    point = createdata()
    WriteToTxt(point,'data.txt')
'''
'''
def insert_sort(list):
    count = len(list)
    for i in range(0,count):
        key = list[i]
        j = i-1
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
                key = list[j]
                k = j - group
                while k>=0:
                    if list[k] > key:
                        list[k+group] = list[k]
                        list[k] = key
                    k -= group
                j += group
        group = int(group/step)
    return list
def quick_sort(list,left,right):
    if left>=right:
        return list
    low = left
    high = right
    key = list[left]
    while left<right:
        while left<right and key<=list[right]:
            right -= 1
        list[left] = list[right]
        while left<right and key>=list[left]:
            left += 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list,low,left-1)
    quick_sort(list,left+1,high)
    return list

if __name__ == '__main__':
    a = [1,3,2,4,5]
    #print(insert_sort(a))
    #print(shell_sort(a))
    print(quick_sort(a,0,4))
'''
'''
def insert_sort(list):
    count = len(list)
    for i in range(0,count):
        key = list[i]
        j = i -1
        while j>=0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1
    return list


def shell_sort(list):
    count = len(list)
    if count<=1:
        return list
    step = 2
    group = int(count/step)
    while group>0:
        for i in range(0,group):
            j = i + group
            while j<count:
                key = list[j]
                k = j - group
                while k>=0:
                    if list[k] >key:
                        list[k+group] = list[k]
                        list[k] = key
                    k -= group
                j += group
        group = int(group/step)
    return list


def bubble_sort(list):
    count = len(list)
    if count <= 1:
        return list
    for i in range(0,count):
        for j in range(i+1,count):
            if list[j] < list[i]:
                list[i],list[j]=list[j],list[i]
    return list

def quick_sort(list,left,right):
    count = len(list)
    if left>=right:
        return list
    low = left
    high = right
    key = list[left]
    while left<right:
        while left<right and key<=list[right]:
            right -= 1
        list[left] = list[right]
        while left<right and key>=list[left]:
            left += 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list,low,left-1)
    quick_sort(list,left+1,high)
    return list

def select_sort(list):
    count = len(list)
    if count<=1:
        return list
    for i in range(0,count):
        k = i
        for j in range(i+1,count):
            if list[j] < list[k]:
                k = j
        list[i],list[k]=list[k],list[i]
    return list

def merge_sort(list):
    count = len(list)
    if count <= 1:
        return list
    mid = int(count/2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left,right)
def merge(left,right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return  result
if __name__ == '__main__':
    a = [1,3,2,5,4]
    #print(insert_sort(a))
    #print(shell_sort(a))
    #print(bubble_sort(a))
    #print(quick_sort(a,0,4))
    #print(select_sort(a))
    print(merge_sort(a))
'''

def insert_sort(list):
    count = len(list)
    for i in range(0,count):
        k = list[i]
        j = i -1
        while j>=0:
            if list[j] > k:
                list[j+1] = list[j]
                list[j] = k
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
                key = list[j]
                k = j - group
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
        for j in range(i,count):
            if list[i] > list[j]:
                list[i],list[j]=list[j],list[i]
    return list
def quick_sort(list,left,right):
    if left>=right:
        return list
    low = left
    high = right
    key = list[left]
    while left<right:
        while left<right and key<=list[right]:
            right -= 1
        list[left] = list[right]
        while left<right and key>=list[left]:
            left += 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list,low,left-1)
    quick_sort(list,left+1,high)
    return list
if __name__ == '__main__':
    a = [2,1,3,5,4]
    #print(insert_sort(a))
    #print(shell_sort(a))
    #print(bubble_sort(a))
    print(quick_sort(a,0,4))






















































'''def insert_sort(lists):
    count = len(lists)
    for i in range(0,count):
        key = lists[i]
        j = i-1
        while(j >= 0):
            if(lists[j] > key):
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists'''

'''def shell_sort(lists):
    count = len(lists)
    step = 2
    group = int(count/step)
    while(group > 0):
        for i in range(0,group):
            j = i + group
            while(j < count):
                k = j - group
                key = lists[j]
                while(k >= 0):
                    if(lists[k] > key):
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group = int(group/step)
    return lists'''

'''def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if (lists[i]>lists[j]):
                lists[i], lists[j] = lists[j], lists[i]
    return lists'''

'''def quick_sort(lists,left,right):
    if (left > right):
        return lists
    key = lists[left]
    low = left
    high = right
    while (left < right):
        while ((left < right) and (lists[right] >= key)):
            right -= 1
        lists[left] = lists[right]
        while ((left < right) and (lists[left] <= key)):
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists'''

'''def merge_sort(lists):
    if (len(lists) <= 1):
        return lists
    middle = int(len(lists)/2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left,right)

def merge(left,right):
    i,j = 0,0
    result = []
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result'''

'''import math
def place(x,k):
    for i in range(0,k):
        if ((x[i] == x[k]) or abs(x[i] - x[k]) == abs(i - k)):
            return False
    return True

def n_queen(x,n):
    k = 0
    x[0] = 0
    flag = False
    while (k>=0):
        while (x[k] <= n):
            if (not place(x,k)):
                x[k] = x[k] + 1
            else:
                if (k == n):
                    print(x)
                    flag = True
                    break
                else:
                    k = k+1
                    x[k] = 0
        if (flag):
            break
        else:
            x[k] = 0
            k = k-1
            x[k] = x[k] +1
    return x'''


if __name__ == '__main__':
    #a = [3,1,2,4]
    a = [0,0,0,0]
    #print(insert_sort(a))
    #print(shell_sort(a))
    #print(bubble_sort(a))
    #print(quick_sort(a,0,3))
    #print(merge_sort(a))
    n_queen(a,3)

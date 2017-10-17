'''import operator
def mergr_sort(lists):
    count = len(lists)
    mid = int(count/2)
    left = mergr_sort(lists[:mid])
    right = mergr_sort(lists[mid:])
    merge(left,right)
def merge(left,right):
    i,j=0,0
    result = []
    while i <len(left) and j <len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append((right[j]))
            j += 1
        elif le'''
import numpy as np
from collections import deque
map = np.matrix([
    [31,28,31,30,31,30,31,31,30,31,30,31],
    [31,29,31,30,31,30,31,31,30,31,30,31]
])
def IsLeap(year):
    if((year%4==0 and year%400!=0) or (year%400==0)):
        return 1
    else:
        return 0

def SumDay(year,month,day):
    t = IsLeap(year)
    sum = 0
    for i in range(0,month-1):
        sum += map[t,i]
    return sum+day
if __name__ == '__main__':
    test = int(input())
    result = []
    while(test>0):
        list = input().split(":")
        year = int(list[0])
        month = int(list[1])
        day = int(list[2])
        result.append(SumDay(year,month,day))
        test -= 1
    #result = ''.join(f+' ' for f in result)
    for i in range(0,len(result)):
        print(result[i])

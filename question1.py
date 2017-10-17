filename = 'D:\\test\\zhongshu.txt'
def loadData(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    lst1 = []
    for line in arrayOLines:
        line = line.strip()
        for i in line:
            if(i!=' '):
             lst1.append(i)
    printZhongshu(lst1)

def printZhongshu(lst1):
    mode = []
    lst1_appear = dict((l,lst1.count(l)) for l in lst1)
    maxN = max(lst1_appear.values())
    for key,value in  lst1_appear.items():
        if value == maxN:
            print(key,value)

if __name__ == '__main__':
    loadData(filename)

'''from math import log
import operator

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    lableCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in lableCounts.keys():
            lableCounts[currentLabel] = 0
        lableCounts[currentLabel] +=1
    shannonEnt = 0.0
    for key in lableCounts:
        prob = float(lableCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt



def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet




def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfGain = 0.0;bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain >bestInfGain):
            bestInfGain = infoGain
            bestFeature = i
    return bestFeature

:
            classCount[vote] = 0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.items(),\
     key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]





def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLable1 = labels[bestFeat]
    myTree = {bestFeatLable1:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLable1][value] = createTree(splitDataSet\
                                                       (dataSet,bestFeat,value),subLabels)
    return myTree


def Treeclassify(inputTree,featLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__=='dict':
                classLabel = Treeclassify(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel



def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()



def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)



import pandas as pd
import xlsxwriter
data = pd.read_excel(io='data.xls',skiprows=2,sheetname=[0,10])
data.cell


def exchangeInformation(lists, colnum):
    global Num
    if colnum == 6:
        if lists == '快乐思维初级上':
            Num = 1.1
        elif lists == '快乐思维初级下':
            Num = 1.2
        elif lists == '快乐思维中级上':
            Num = 2.1
        elif lists == '快乐思维中级下':
            Num = 2.2
        elif lists == '快乐思维高级上':
            Num = 3.0
        else:
            Num = 0
    elif colnum == 8:
        if lists == '一':
            Num = 1.0
        elif lists == '二':
            Num = 2.0
        elif lists == '三':
            Num = 3.0
        elif lists == '四':
            Num = 4.0
        elif lists == '五':
            Num = 5.0
        elif lists == '六':
            Num = 6.0
        else:
            Num = 0
    elif colnum == 10:
        if lists == 'yes':
            Num = 1
        else:
            Num = 0
    return Num


def writeToTxt(list_name, file_path):
    fp = open(file_path, "w+")
    len = 0
    for item in list_name:
        len = len + 1
        if len % 4 == 0:
            fp.write(str(item) + '\n')
        else:
            fp.write(str(item) + ',')
    fp.close()

import xlrd
import numpy as np
bk = xlrd.open_workbook('data.xlsx')
sh = bk.sheet_by_name("万琳")
nrows = sh.nrows
ncols = sh.ncols
row_list = []
data1 = []
for i in range (2,nrows):
    for j in range(1,ncols):
        if j == 6 or j ==8 or j == 9 or j == 10:
            row_data = sh.cell_value(i,j)
            data = exchangeInformation(row_data,j)
            data1.append(data)





import xlrd
import xlwt
import os
filename = 'data2.xlsx'

data = xlrd.open_workbook(filename)
sheet = data.get_sheets(0)
sheet.write(1,2,'0.5')
os.remove(filename)
data.save(filename)

import xlrd
import xlwt
data = xlrd.open_workbook('m.xlsx')
table = data.sheet_by_name("Sheet1")
table.row_values(1)
workbook = xlwt.Workbook(encoding="ascii")
worksheet = workbook.add_sheet('s')
worksheet.write(table.row_values(1))
workbook.save('mm.xlsx')
'''
import xlrd
import xlwt
bk = xlrd.open_workbook('data.xlsx')
sh = bk.sheet_by_name("Sheet1")
nrows = sh.nrows
ncols = sh.ncols
result = []
Aresult, Cresult, Uresult = [], [], []

def B(r1,r2,j,g,m):
    def A1(t,p1t,wt,j):
        mid1 = wt*p1t*((1/(1+j))**(t-22))
        return mid1
    def A2(t,p2t,wt,j):
        mid2 = wt*p2t*((1/(1+j))**(t-22))
        return mid2
    sum1,sum2,sum11,sum22,sum111,sum222=0.0,0.0,0.0,0.0,0.0,0.0
    row_list = []
    row_data1 = []
    for i in range(1, r1-22+1):
            mid1 = A1(float(sh.cell_value(i,0)),float(sh.cell_value(i,1)),float(sh.cell_value(i,3)),j)
            sum1 += mid1
    for i in range(1,r2-22+1):
            mid2 = A1(float(sh.cell_value(i,0)),float(sh.cell_value(i,2)),float(sh.cell_value(i,3)),j)
            sum2 += mid2
            #C(sh.cell_value(i,0),sh.cell_value(i,1),sh.cell_value(i,2),sh.cell_value(i,3))
    A = 0.28 * 1.5*(sum1 + sum2)

    for i in range(r1,101):
        wr1 = float(sh.cell_value(r1-22,3)) * (r1-37)*((1+0.4*g)**(i-r1))*\
        float(sh.cell_value(i-22+1,1))*((1/(1+j))**(i-22))
        sum11 += wr1
    for i in range(r2,101):
        wr2 = float(sh.cell_value(r2 - 22, 3)) * (r2 - 37) * ((1 + 0.4*g) ** (i - r2)) * \
              float(sh.cell_value(i-22+1, 2)) * ((1 / (1 + j)) ** (i - 22))
        sum22 += wr2

    wr = 0.01*(sum11+sum22)
    for i in range(r1,101):
        wr11 = float(sh.cell_value(r1-22,3))*(1+j)*\
        (((1+g)**(r1-22) - (1+j)**(r1-22))\
          /( (g-j)*( (1+g)**(r1-23) ) ))*((1+0.4*g)**(i-r1))*\
               float(sh.cell_value(i-22+1,1))*((1/(1+j))**(i-22))
        sum111 += wr11

    for i in range(r2,101):
        wr22 = float(sh.cell_value(r2 - 22, 3)) * (1 + j) * \
               (((1 + g) ** (r2 - 22) - (1 + j) ** (r2 - 22)) \
                / (( g - j) * ((1 + g) ** (r2 - 23)))) * ((1 + 0.4 * g) ** (i - r2)) * \
               float(sh.cell_value(i-22+1, 1)) * ((1 / (1 + j)) ** (i-22))
        sum222 += wr22
    #m = 15
    #print(sum111)
    wr2 = (0.08/m)*(sum111+sum222)
    C = wr+wr2
    U = C-A
    '''
    print("A="+A)
    print("C="+C)
    print("U="+U)
    '''
    return A,C,U
def A():
    for i in range(1,2):
        r1 = int(sh.cell_value(i,9))
        r2 = int(sh.cell_value(i,10))
        j = float(sh.cell_value(i,11))
        g = float(sh.cell_value(i,12))
        m = int(sh.cell_value(i,13))
        A,C,U = B(r1,r2,j,g,m)
        A = ("%.2f" % A)
        C = ("%.2f" % C)
        U = ("%.2f" % U)
        result.append(A)
        result.append(C)
        result.append(U)

'''

if __name__ == '__main__':
    r1 = int(input())
    r2 = int(input())
    j = float(input())
    g = float(input())
    B(r1,r2,j,g)
'''





'''
####写进txt里面
def writeToTxt(list_name, file_path):
    fp = open(file_path, "w+")
    len = 0
    for item in list_name:
        fp.write(str(item) + '\n')
    fp.close()

'''
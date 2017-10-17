from numpy import  *
import operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlable = labels[sortedDistIndicies[i]]
        classCount[voteIlable] = classCount.get(voteIlable,0) + 1
    sortedClassCount = sorted(classCount.items(),
     key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def fileMatrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat =zeros((numberOfLines,3))
    classLableVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip();
        #listFromLine = line.split('\t')
        listFromLine = line.split(',')
        returnMat[index,:] = listFromLine[0:3]
        classLableVector.append(float(listFromLine[-1]))
        index +=1
    return returnMat,classLableVector

import matplotlib
import  matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDatMat[:,1], datingDataMat[:,2])
plt.show()




def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet,ranges,minVals




def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLables = fileMatrix('datingTestSet.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i,:],normMat[numTestVecs:m,:],datingLables[numTestVecs:m],3)
        print ("the classifer came back with: %d,the real answer is: %d"%(classifierResult,datingLables[i]))
        if (classifierResult != datingLables[i]): errorCount += 1.0
    print("the total error rate is : %f" % (errorCount/float(numTestVecs)))



def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percenTats = float(input("percentage of time spent playing vedio games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLables = fileMatrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percenTats,iceCream])
    classfierResult = classify((inArr-minVals)/ranges,normMat,datingLables,3)
    print("You will probably like this person：",resultList[classfierResult -1])


















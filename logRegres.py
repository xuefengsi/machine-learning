import  random
import math
import matplotlib as plt
from numpy import *

#随机生成100个二维数据



def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('C:\\Users\\sxf\\Desktop\\机器学习\\logdata.txt')
    for line in fr.readlines():
        lineArr = line.strip().split(',')
        dataMat.append([1.0,float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat


def sigmoid(inX):
    return 1.0/(1 + math.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix =mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = (labelMat - h)
        weights =  weights + alpha * dataMatrix.transpose() * error
    return weights

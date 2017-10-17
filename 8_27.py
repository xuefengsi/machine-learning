'''def findArrayMex(A, n):
    # write code here
    m = max(A)
    for i in range(1,m):
        if i not in A:
            return i
        '''
'''
def findMaxDivision( A, n):
    import numpy as np
    m = max(A)
    h = 0
    B = []
    C = []
    for i in range(0,m):
        B.append(h)
    for i in range(0,n):
        B[A[i]-1] += 1
    for i in range(0,m):
        if B[i] != 0:
            C.append(i+1)
    Blen = len(C)
    result = 0
    for i in range(0,Blen-1):
        j=i+1
        if C[j] - C[i] > result:
            result = C[j] - C[i]
    return result



if __name__ == '__main__':
    A=(input()).split(" ")
    Alen = len(A)
    B = []
    for i in range(0,Alen):
        mid = int(A[i])
        B.append(mid)
    
    B = [9,1,3,10]
    #print(findArrayMex(A,4))
    print(findMaxDivision(B,len(B)))
    '''
'''
import numpy as np
def rotateMatrix( mat, n):
    import numpy as np
    mid = np.zeros((n,n))
    result = np.zeros((n,n))
    #result = [n+1][n+1]
    for i in range(0,n):
        for j in range(0,n):
            mid[j,n-i-1] = int (mat[i,j])
            result[j,n-i-1]
    return (type(mid[0][0]))

if __name__ == '__main__':
    mat = np.matrix([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    print(mat)
    print(rotateMatrix(mat,3))
'''

'''
#求之字形的矩阵
def printMatrix( mat, n, m):
    result = [['' for x in range(m)] for y in range(n)]
    for i in range(0, n):
        for j in range(0, m):
            if (i + 1) % 2 == 0:
                result[i][m - j - 1] = mat[i][j]
                print(result[i][m - j - 1])
            else:
                result[i][j] = mat[i][j]
    A = []
    for i in range(0, n):
        for j in range(0, m):
            A.append(result[i][j])
    return A
if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    print(type(mat))
    print(printMatrix(mat,4,3))
'''
'''
#字符串反转
def rotateString( A, n, p):
    from collections import deque
    A=list(A)
    A.reverse()
    B = A[:n-p-1]
    C = A[n-p-1:]
    B.reverse()
    C.reverse()
    result = B+C
    result = ''.join(f+'' for f in result)
    return result
if __name__ == '__main__':
    A = "12345678"
    print(rotateString(A,8,5))

'''
'''
#数组从右上角到左下角打印
def arrayPrint(arr, n):
    row = 0
    col = n-1
    res = []
    while row<n:
        i = row
        j = col
        while i<n and j<n:
            res.append(arr[i][j])
            i += 1
            j += 1
        if col>0:
            col -= 1
        else:
            row += 1
    return res
if __name__ == '__main__':
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(arrayPrint(a,4))
'''








































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

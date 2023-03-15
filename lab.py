# p5 4 - WAP to implement matrix multiplication
mat1 = list()
mat2 = list()
raw = int(input('Raw: '))
column = int(input('column: '))
# function to take matrix as input
def matcollect(r,c,typ=''):
    returnlist = list()
    for i in range(0,r):
        tempList = list()
        for j in range(0,c):
            if typ == 'nor':
                tempList.append(0)
            else:
                tempList.append(int(input(f"{i+1}x{j+1} : ")))
                
        returnlist.append(tempList)
    return returnlist
print('first matrix:')
mat1 = matcollect(raw,column)
print('second matrix:')
mat2 = matcollect(raw,column)
mat3 = matcollect(raw,column,typ='nor')
# multiplying
for i,f in enumerate(mat1):
    for j,iner in enumerate(f):
        for c,asiehi in enumerate(f):
            mat3[i][j] += mat1[i][c]*mat2[c][j]
print('output')
for q in mat3:
    print(q)
#Useful Matrix Functions
def printM (M) :
    matrixString = ""
    for row in M :
        for element in row :
            matrixString += "[" + str(element) + "]\t"
        matrixString += "\n"
    print(matrixString)

def rowMultiply(row, scalar) :
    index = 0
    while index < len(row) :
        row[index] *= scalar
        index+=1
def rowAdd(row1, row2, scalar) :
    temp = row1.copy()
    if scalar != 1 :
        rowMultiply(temp,scalar)
    index = 0
    while index < len(row2) :
        row2[index] += temp[index]
        index+=1
def swapRow(MIn, row1, row2) :
    temp = MIn[row1].copy()
    MIn[row1] = MIn[row2].copy()
    MIn[row2] = temp

def determinate(MIn) :
    if len(MIn) <= 1 :
        return MIn[0][0]
    ans = 0
    for column in range(len(MIn[0])) :
        newMatrix = [None] * (len(MIn) - 1)
        for row in range(len(MIn)-1) :
            newMatrix[row] = [None] * (len(MIn[row]) - 1)
        for newRow in range(len(MIn)-1) :
            for newColumn in range(len(MIn[0])-1) :
                if newColumn < column :
                    newMatrix[newRow][newColumn] = MIn[newRow+1][newColumn]
                else :
                    newMatrix[newRow][newColumn] = MIn[newRow+1][newColumn+1]
        ans += MIn[0][column] * (((column%2)*-2)+1) * determinate(newMatrix)
    return ans
def rowEchelon(MIn) :
    index = 0
    while index < len(MIn) :
        elementToAdd = MIn[index][index]
        nextRow = index + 1
        while nextRow < len(MIn) :
            if elementToAdd != 0 :
                elementToRemove = MIn[nextRow][index]
                scalarToRemove = elementToRemove / ((1.0)*elementToAdd)
                rowAdd(MIn[index], MIn[nextRow], -1 * scalarToRemove)
                nextRow += 1
            else :
                if MIn[nextRow][index] != 0 :
                    elementToAdd = MIn[nextRow][index]
                    swapRow(MIn, nextRow, index)
                    nextRow = index + 1
                else :
                    nextRow += 1
        index += 1
def rowReduce(MIn) :
    index = 0
    while index < len(MIn) :
        rowMultiply(MIn[index], 1.0/MIn[index][index])
        index+=1
def reducedEchelon(MIn) :
    index = 1
    while index < len(MIn) :
        elementToAdd = MIn[index][index]
        nextRow = index - 1
        while nextRow >= 0 :
            if elementToAdd != 0 :
                rowAdd(MIn[index], MIn[nextRow], -1 * MIn[nextRow][index])
                nextRow -= 1
            else :
                if MIn[nextRow][index] != 0 :
                    elementToAdd = MIn[nextRow][index]
                    swapRow(MIn, nextRow, index)
                    nextRow = index - 1
                else :
                    nextRow -= 1
        index += 1
def PrintLUDecomposition(MIn) :
    U = [None] * len(MIn)
    for index in range(len(MIn)):
        U[index] = MIn[index].copy()
    L = [None] * len(MIn)
    for row in range(len(MIn)) :
        L[row] = [0] * len(MIn[row])
    for diagonal in range(len(MIn)) :
        L[diagonal][diagonal] = 1
    index = 0
    while index < len(U) :
        elementToAdd = U[index][index]
        nextRow = index + 1
        while nextRow < len(U) :
            if elementToAdd != 0 :
                elementToRemove = U[nextRow][index]
                scalarToRemove = elementToRemove / ((1.0)*elementToAdd)
                L[nextRow][index] = scalarToRemove
                rowAdd(U[index], U[nextRow], -1 * scalarToRemove)
                nextRow += 1
            else :
                if U[nextRow][index] != 0 :
                    elementToAdd = U[nextRow][index]
                    swapRow(U, nextRow, index)
                    nextRow = index + 1
                else :
                    nextRow += 1
        index += 1
    printM(L)
    printM(U)
def isDiagonallyDominant(MIn) :
    for column in range(len(MIn)) :
        sumCol = 0
        for row in range(len(MIn[column])) :
            if row != col :
                sumCol += MIn[row][column]
        if sumCol > MIn[column][column] :
            return false
    return true
def isSquare(MIn) :
    return len(MIn) == len(MIn[0])
def isSymmetric(MIn) :
    for row in range(len(MIn)) :
        for column in range(lenMIn[0]) :
            if MIn[row][column] != MIn[column][row] :
                return false
    return true

#Test Input
def function(t, y):
    return t-(y*y)
a = 0
b = 2
N = 10
h = ((b-a)*(1.0))/N
w0 = 1

matrix1 = [[2, -1, 1, 6],[1,3,1,0], [-1, 5, 4, -3]]

matrix2 = [[1, 1, 0, 3],[2,1,-1,1], [3, -1, -1, 2], [-1, 2, 3, -1]]

#Question 1
w = w0
index = 0
ti = a
while(index<N):
    ti = (a+(index*h))
    w = (w + (function(ti,w)*h))
    index+=1
print(str(w)+"\n")
#Question 2
w = w0
index = 0
ti = a
while(index<N):
    ti = a+(index*h)
    k1 = function(ti,w) * h
    k2 = function(ti+(h/2),w+(k1/2)) * h
    k3 = function(ti+(h/2),w+(k2/2)) * h
    k4 = function(ti+h,w+k3) * h
    w = w + ((k1+(2*k2)+(2*k3)+k4)/6)
    index+=1
print(str(w)+"\n")

#Question 3
rowEchelon(matrix1)
rowReduce(matrix1)
reducedEchelon(matrix1)
answer = "["
for row in range(len(matrix1)) :
    if row!=0 :
        answer+=" "
    answer+=str(int(matrix1[row][len(matrix1[row])-1]))
answer += "]"
print(answer)
print()

#Question 4
print(determinate(matrix2))
print()
PrintLUDecomposition(matrix2)
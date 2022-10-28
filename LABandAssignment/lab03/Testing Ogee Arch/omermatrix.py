# TYPES OF MATRIX-----------

def isNullMatrix(A):
    boolean = True
    for i in A:
        for j in i:
            if j != 0:
                boolean = False
    if boolean == True:
        print("null matrix")
    else:
        print("not null matrix")


def isSquareMatrix(A):
    row, column = countMatrix(A)
    if row == column:
        print("Square matrix")
    else:
        print("not a square matrix")


def isUnitMatrix(A):
    row, column = countMatrix(A)
    if row == column:
        boolean = True
        a = 0
        b = 0
        for i in A:
            for j in i:
                if a == b:
                    if A[a][b] != 1:
                        boolean = False
                else:
                    if A[a][b] != 0:
                        boolean = False
                b += 1
            b = 0
            a += 1
        if boolean == True:
            print("It is an unit matrix")
        else:
            print("not an unit matrix")
    else:
        print("not an unit matrix because it isn't a square matrix")


def isIdentityMatrix(A):
    boolean = True
    a = 0
    b = 0
    for i in A:
        for j in i:
            if a == b:
                if A[a][b] != 1:
                    boolean = False
            else:
                if A[a][b] != 0:
                    boolean = False
            b += 1
        b = 0
        a += 1
    if boolean == True:
        print("It is an unit matrix")
    else:
        print("not an unit matrix")


def isDiagonalMatrix(A):
    row, column = countMatrix(A)
    if row == column:
        boolean = True
        a = 0
        b = 0
        for i in A:
            for j in i:
                if a != b:
                    if A[a][b] != 0:
                        boolean = False
                b += 1
            b = 0
            a += 1
        if boolean == True:
            print("It is a diagonal matrix")
        else:
            print("not a diagonal matrix")
    else:
        print("not a diagonal matrix because it isn't a square matrix")


def isScalarMatrix(A):
    row, column = countMatrix(A)
    if row == column:
        boolean = True
        a = 0
        b = 0
        same = A[0][0]
        for i in A:
            for j in i:
                if a == b:
                    if A[a][b] != same:
                        boolean = False
                else:
                    if A[a][b] != 0:
                        boolean = False
                b += 1
            b = 0
            a += 1
        if boolean == True:
            print("It is a Scalar matrix")
        else:
            print("not a Scalar matrix")
    else:
        print("not a Scalar matrix because it isn't a square matrix")


# CREATING, PRINITING, CHECKING ROWS AND COLUMN--------


def createMatrix(row, column):
    matrix = []
    for i in range(row):
        columnMatrix = []
        for j in range(column):
            columnMatrix.append(float(input(f"matrix[{i+1}][{j+1}]: ")))
        matrix.append(columnMatrix.copy())
    return matrix


def createEmptyMatrix(row, column):
    matrix = []
    for i in range(row):
        columnMatrix = []
        for j in range(column):
            columnMatrix.append(0)
        matrix.append(columnMatrix.copy())
    return matrix


def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end="    ")
        print("\n")


def countMatrix(matrix):
    row = 0
    for i in matrix:
        row += 1
        column = 0
        for j in i:
            column += 1
    return row, column


# OPERATION ON MATRIX---------


''' ADDITION '''
def addMatrix(matrix1, matrix2):
    matrix = []
    rowMatrix = []
    row1, a = countMatrix(matrix1)
    row2, b = countMatrix(matrix2)
    if row1 == row2 and a == b:
        for i in range(row1):
            rowMatrix = []
            for j in range(b):
                 rowMatrix.append(matrix1[i][j] + matrix2[i][j])
            matrix.append(rowMatrix.copy())
        return matrix
    else:
        return "not possible"


''' SUBTRACTION '''
def subtractMatrix(matrix1, matrix2):
    matrix = []
    rowMatrix = []
    row1, a = countMatrix(matrix1)
    row2, b = countMatrix(matrix2)
    if row1 == row2 and a == b:
        for i in range(row1):
            rowMatrix = []
            for j in range(b):
                 rowMatrix.append(matrix1[i][j] - matrix2[i][j])
            matrix.append(rowMatrix.copy())
        return matrix
    else:
        return "not possible"


''' MULTIPLICATION '''
def multiplyMatrix(A, B):
    rowOfA, columnOfA = countMatrix(A)
    rowOfB ,columnOfB = countMatrix(B)
    if columnOfA == rowOfB:
        matrix = createEmptyMatrix(rowOfA, columnOfB)
        for i in range(rowOfA):
            m = []
            for j in range(columnOfB):
                for k in range(columnOfA):
                    matrix[i][j] += (A[i][k]*B[k][j])
        return matrix
    else:
        return "Multiplication not possible"


''' TRANSPOSE '''
def transposeMatrix(A):
    row, column = countMatrix(A)
    B = createEmptyMatrix(column, row)
    a = 0
    b = 0
    for i in A:
        for j in i:
            B[b][a] = j
            b += 1
        b = 0
        a += 1
    return B


''' MULTIPLY WITH SCALAR '''
def multiplyScalarMatrix(matrix, scalar_quantity):
    newMatrix = []
    for i in matrix:
        holder = []
        for j in i:
            holder.append(j*scalar_quantity)
        newMatrix.append(holder)
    return newMatrix

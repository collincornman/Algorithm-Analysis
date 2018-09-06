import numpy
import sys
with open(sys.argv[1]) as f:
    i = 0
    n = int(f.readline())
    # Generate a matrix with an extra column to hold vector b
    matrix = numpy.zeros((n, n + 1))

    while i < n:
        # Split line
        line = f.readline()
        tokens = line.split()

        for j in range (0, n):
            # Put each coefficient of x inside the matrix
            matrix[i][j] = tokens[j]
        i += 1
    # Reading the last line seperately, store each value of vector b in the correct order
    vector = f.readline()
    tokens = vector.split()
    for j in range (0, n):
        # Put each value of equation into the last column of the matrix
        matrix[j][n] = tokens[j]

def magFind(matrix,high):
    max = float(matrix[0][0])
    for x in range(1,high):
        if float(matrix[x][0]) > max:
            max = float(matrix[x][0])
    if max != float(matrix[0][0]):
        for x in range(1,high):
            if float(matrix[x][0]) == max:
                matrix[[0, x]] = matrix[[x, 0]]

    return matrix

matrix = magFind(matrix,n)

def reF(low, low2, high, matrix):
    for x in range(low,high):
        for y in range(low2,high+1):
            if matrix[x][y] != 0:
                matrix[x][y] = matrix[x][y] - matrix[low2][y]
    return matrix


def rowRed(low, high, matrix):
    for x in range(low,n):
        if matrix[x][high]!= 1.0:
            src = matrix[x][low]
            for y in range(low, high+1):
                if src == 0.0:
                    if x == low:
                        break
                    else:
                        sys.exit("System is inconsistent")
                else:
                    matrix[x][y] = matrix[x][y]/src
    return matrix

for x in range(0,n):
    matrix = rowRed(x,n,matrix)
    matrix = reF(x+1,x,n,matrix)

def isValid(matrix):
    bool = True
    for x in matrix:
        sum = 0
        for y in range(len(x)-1):
            sum += y
        if sum == 0.0:
            bool = False
    return bool

def solve(high, matrix):
    val = []
    s = list()
    for x in reversed(matrix):
        s.append(x)
    for x in range(0,high):
        for y in range(0, high):
            if not val:
                if float(s[x][high-1]) == 0.0:
                    sys.exit("System is incon")
                else:
                    val.append(s[x][high])
            else:
                bol = False
                var = 0
                if (float(s[x][y]) != 0.0) and (float(s[x][y]) != 1.0):
                    for z in range(len(val)):
                        if y == high:
                            break
                        var += (s[x][y] * val[z])
                        y+=1
                        bol = True
                if bol:
                    var = s[x][high] - var
                    val.insert(0, var)
                    break
    for x in range(len(val)):
        val[x] = "{0:.3f}".format(val[x])
        val[x] = float(val[x])
    print(val)

if isValid(matrix):
    solve(n,matrix)
else:
    print("No solution exists")


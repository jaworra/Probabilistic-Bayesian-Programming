'''
Implemenation of standard mathematical operations
'''


import numpy as np

# Summation  
x = [1, 2, 3, 4, 5, 6]
result = 0
for i in range(6):
    result += x[i]
print(result)
#or
result = 0
for i,val in enumerate(x):
    result += val
print(result) # 21

# Product
x = [1, 2, 3, 4, 5, 1]
result = 1
for i in range(6):
    result *= x[i]
print(result) # 120

# Factorial
result = 1
for i in range(1,6):
    result *= i
print(result) # 120


# Conditional Brackets
i = 3
y = [-2, 3, 4, 1]
result = 0
if i in y:
    result = sum(y)
elif i > 0:
    result = 1
else:
    result = 0
print(result) # -> 6


# Element Wise matrix multiplication (requires same size matrix) 
y = [[2,1],[4,3]]
z = [[1,2],[3,4]]
x = [[0,0],[0,0]] #output
for i in range(len(y)):
    for j in range(len(y[0])):
        x[i][j] = y[i][j] * z[i][j]
print(x)# -> [[2, 2], [12, 12]]

# Cartesian Matrix Multiplication
m1 = np.array([[1, 2, 3],[4, 5, 6] ])
m2 = np.array([[7, 8],[9, 10],[11, 12]])
r = np.array([[0, 0],[0, 0]])
s = 0
for i in range(2):
    for j in range(2):
        for k in range(3):
            s = s + m1[i][k]*m2[k][j]
        r[i][j] = s
        s = 0
print(r)
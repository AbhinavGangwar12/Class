# PYTHON PROGRAM TO WORK WITH SCALARS

import numpy as n
from numpy import *
from random import randint as r
# x = n.array([[1],[2],[3]])

# y = n.array([[3],[2],[5]])

# print(x.shape)
# print(y.shape)
# print(f"3D vector : \n{x}")
# print(f"3D vector : \n{y}")
# z = x*y
# print(f"product 3D vector : \n{z}")

# a = n.array([[1,2,3],
#              [4,6,8],
#              [8,9,3]
#              ])

# b = n.array([[1,2,3],
#              [4,6,8],
#              [8,9,3]
#              ])


# print(f"dimensions : {a.shape}")

# print(f"Matrix 1 : \n{a}\n")
# a *= 3
# print(f"Matrix 1 after scaling with 3: \n{a}\n")

# print(f"Matrix 2 : \n{b}\n")
# print(f"Matrix 1 + Matrix 2 : \n{n.add(a,b)}\n")
# print(f"Matrix 1 * Matrix 2 : \n{n.multiply(a,b)}\n")
# print(f"Matrix 1 * Matrix 2 : \n{a*b}\n")

alpha = r(1,11)
beta = r(1,11)

m1 = n.array([
    [2],
    [4],
    [6]
])
m2 = n.array([
    [24],
    [14],
    [1]
])

# multiplication = n.add(n.multiply(alpha,m1),n.multiply(beta,m2))

# print(f"alpha * matrix1 + beta * matrix2 :\n{multiplication}")
# print(f"Size of new matrix : {multiplication.size}")

# print(f"Transpose of matrix 1 : {m1.T}")

# dot_product = m1.T@m2#Method--1
# dot_product_ = n.dot(m1.T,m2)#Method--2
# #Method 1 and 2 are same
# print(f"Dot product of matrix 1 and matrix 2 :\n{dot_product}")


# NORMs 
# there are three methods to find norms
# --Eucledean norm <L2 norm>: nearest distance between two vectors <L2 nom> -> under_root( submission(i = 1, x) Xi ^ 2 ) {||x||2}
# --Manhattan norm <L1 norm> : absolute distance between two vectors -> submission(x=1,infinite)|Xi| {||x||1}
# --Max norm <> : maximum value of the vector -> max_i|Xi| ( for all value of 'i' )

m3 = n.array([
    [1],
    [-2]
])

m4 = n.array([
    [5],
    [7]
])

# Linear Algorithm = linalg
# numpy.linalg.norm(matrix_array, norm_form) --> norm_form :{ 2 (Eucledean norm), 1 (Manhattan norm) , numpy.inf (Max norm)}

# print(f"Eucledean norm : {n.linalg.norm(m3,2)}") #Used to find shortest distance
# print(f"Manhattan norm : {n.linalg.norm(m3,1)}")
# print(f"MAx norm : {n.linalg.norm(m3,n.inf)}")

print(f"Distance between {m3} and {m4} : {n.linalg.norm(m3-m4,2)}")
cos_theta = (m3.T@m4) / ( n.linalg.norm(m3,2) * n.linalg.norm(m4,2) ) # cos_theta = x(T).y / ||x||2 * ||y||2
print(f"Cosine of\n{m3}\nand\n{m4} : {n.round(cos_theta,3)}")

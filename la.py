#!/usr/bin/env python3
from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    """solve(A,b)
    A- matrix m*k
    b- matrix k*2
    x- list of solusion []

    using Gauss Method with numpy
    1.กำจัดจุดอ่อน -elimination
    2.แทนคำย้อนกลับ -back substitution
    """
    # YOUR CODE HERE
    import numpy as np
    A,b = np.array(A), np.array(b)
    n = len(A[0])
    x=np.array([0]*n)
    #1.elimination
    for k in range(n-1): #pivot eq #k `ทำให้ตัวแปลหายไป`
        for j in range(k+1, n):
            #print(f'\tกำจัดตัวแปรที่ {k},กำจัดตัวแปรที่{j}')
            lam = A[j][k]/A[k][k]
            #update A[j][k เป็นต้นไป]
            A[j,k:n] = A[j,k:n] - lam*A[k,k:n]
            #print(f'\t\tlambda={lam}')
            #update b[j]
            b[j] = b[j] - lam*b[k]
        #printm(A)
        #print(b)

    #2.ack substitution
    #x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-1, -1, -1):
        #print(f'k={k}')
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n]))/A[k,k]
        
    return x.flatten()

#print('==== A ====')
#printm(A)
#print('==== b ====')
#printm(b)
print(solve(A,b))

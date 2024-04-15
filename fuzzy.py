import numpy as np


def union(A, B):
    result = {}
    for i in A:
        if A[i] > B[i]:
            result[i] = A[i]
        else:
            result[i] = B[i]
    print("Union of two sets is", result, '\n')


def intersection(A, B):
    result = {}
    for i in A:
        if A[i] < B[i]:
            result[i] = A[i]
        else:
            result[i] = B[i]
    print("Intersection of two sets is", result, '\n')


def complement(A, B):
    result = {}
    result1 = {}
    for i in A:
        result[i] = round(1 - A[i], 2)
    for i in B:
        result1[i] = round(1 - B[i], 2)
    print("Complement of  1st set is", result)
    print("Complement of  2nd set is", result1, '\n')


def difference(A, B):
    result = {}
    for i in A:
        result[i] = round(min(A[i], 1 - B[i]), 2)
    print("Difference of two sets is", result, '\n')


def cartprod(A, B):
    R = [[] for i in range(len(A))]
    i = 0
    for x in A:
        for y in B:
            R[i].append(min(A[x], B[y]))
        i += 1
    print("Cartesian Product is", R, "\n")


def maxmin():
    R = [[0.5, 0.8, 0.2], [0.3, 0.6, 0.4]]
    S = [[0.7, 0.4], [0.5, 0.6], [0.2, 0.8]]

    print("\nR:", R)
    print("S:", S)

    m, n = len(R), len(R[0])
    o = len(S[0])
    composition = np.zeros((m, o))

    for i in range(m):
        for k in range(o):
            composition[i][k] = max([min(R[i][j], S[j][k]) for j in range(n)])

    return composition


A = {'a': 0.5, 'b': 0.8, 'c': 0.2}
B = {'a': 0.7, 'b': 0.4, 'c': 0.6}

print(A)
print(B)
print('\n')

union(A, B)
intersection(A, B)
complement(A, B)
difference(A, B)
cartprod(A, B)

result = maxmin()
print("Max-Min Composition is", result)

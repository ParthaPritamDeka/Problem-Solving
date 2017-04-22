def merge(A,B):
    C = {}
    for i in A:
        if i in B:
            if isinstance(A[i], dict):
                print A[i]
                if isinstance(B[i], dict):
                    print B[i]
                    b = merge(A[i],B[i])
                    C[i] = b
                else:
                    pass
            else:
                if A[i]>B[i]:
                    C[i] = A[i]
                else:
                    C[i] = B[i]
        else:
                C[i] = A[i]
    for j in B:
        if j not in A:
            C[j] = B[j]
    
    return C

X = {'a':1, 'b':2, 'c':{'a':1, 'm':5, 'x':7, 'n':9}, 'd':4}
Y = {'a':2, 'b':3, 'c':{'x':1}}
merge(X, Y)
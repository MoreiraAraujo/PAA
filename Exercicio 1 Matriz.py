def encontrar_elemento(mat, X):
    i, j = 0, 0  
    
    while i < len(mat) and j < len(mat[0]):
        if mat[i][j] == X:
            return 1  
        elif mat[i][j] < X:
            j += 1  
        else:
            i += 1  
    
    return 0  

mat = [
    [10, 20, 30],
    [15, 25, 35],
    [27, 29, 37]

]

X = 10
print(encontrar_elemento(mat, X))
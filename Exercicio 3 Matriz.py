def imprimir_serpente(mat, N):
  
    for i in range(N):
        if i % 2 == 0:
            for j in range(N):
                print(mat[i][j], end=" ")
        else:
            for j in range(N-1, -1, -1):
                print(mat[i][j], end=" ")
        
        print()

# Exemplo de uso
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
N = 4

imprimir_serpente(matriz, N)

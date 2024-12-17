def encontrar_lideres(arr):
    n = len(arr)
    lideres = []
    
    maior_direita = arr[-1] 
    lideres.append(maior_direita)
    
    
    for i in range(n - 2, -1, -1):
        if arr[i] >= maior_direita:
            lideres.append(arr[i])
            maior_direita = arr[i]
    
    
    return lideres[::-1]

# Exemplo de uso
arr = [16, 17, 4, 3, 5, 2]
print(encontrar_lideres(arr))  

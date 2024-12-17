def encontrar_elemento_faltante(arr, n):
   
    soma_total = n * (n + 1) // 2
    
    soma_array = sum(arr)
    
    return soma_total - soma_array

# Exemplo de uso
arr = [1, 2, 4, 5, 6]
n = 6
print(encontrar_elemento_faltante(arr, n))

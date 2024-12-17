def segundo_maior(arr):
    maior = segundo_maior = -1
    
    for num in arr:
        if num > maior:
            segundo_maior = maior
            maior = num
        elif num > segundo_maior and num < maior:
            segundo_maior = num
    
    return segundo_maior

# Exemplo de uso
arr = [2, 1, 3, 5, 3]
print(segundo_maior(arr))  

# Exemplo de uso
arr = [3, 10, 7, 5, 8]
print(segundo_maior(arr))  

# Exemplo de uso
arr = [20, 10, 6, 15, 13]
print(segundo_maior(arr)) 
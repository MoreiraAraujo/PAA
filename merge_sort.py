def merge_sort(lista):
 
    if len(lista) <= 1:
        return lista
        
    
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0
    
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
 
    
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

# Exemplo de uso
lista = [1, 2, 3, 3, 6, 9, 82, 10]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

# Exemplo de uso 2
lista = [2, 25, 34, 3, 9, 23, 1]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)

# Exemplo de uso 3
lista = [20, 15, 10, 3, 9, 100, 10]
print("Lista original:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)


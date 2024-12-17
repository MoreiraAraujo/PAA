def soma_vetor(vetor):
    
    if len(vetor) == 0:
        return 0
   
    else:
        return vetor[0] + soma_vetor(vetor[1:])

# Exemplo de uso
vetor = [1, 2, 3, 4, 5]
resultado = soma_vetor(vetor)
print("A soma dos elementos do vetor é:", resultado)

# Exemplo de uso
vetor = [7, 0, 1, 3, 6]
resultado = soma_vetor(vetor)
print("A soma dos elementos do vetor é:", resultado)

# Exemplo de uso
vetor = [1, 9, 2, 5, 8]
resultado = soma_vetor(vetor)
print("A soma dos elementos do vetor é:", resultado)
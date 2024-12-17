
def Arry(A):
    if len(A)==0:
        return 0
    else:
        return A[0]+Arry(A[1:])
    
# Exemplo de uso 1    
Lista=[1,2,3,4,5]
Resultado=Arry(Lista)
print(Resultado)

# Exemplo de uso 2
Lista=[1,2,3,4,5]
Resultado=Arry(Lista)
print(Resultado)

# Exemplo de uso 3
Lista=[1,14,12,6,4]
Resultado=Arry(Lista)
print(Resultado)
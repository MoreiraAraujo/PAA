
def Arry(A):

    if not A:
        return 0

    if len(A)==1:
        return A[0]
    
    return (A[0]+(Arry(A[1:])*(len(A)-1)))/len(A)
 # Exemplo de uso 2   
lsita=[1,2,3,4,5]
resultado=Arry(lsita)
print(resultado)

 # Exemplo de uso 2   
lsita=[1,8,4,9,12,2]
resultado=Arry(lsita)
print(resultado)

 # Exemplo de uso 3   
lsita=[4,2,5,3,2]
resultado=Arry(lsita)
print(resultado)

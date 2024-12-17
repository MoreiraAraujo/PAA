def Arry(A):
   
    for i in range (len(A)):
        min=float("inf")
        minj=0
        for j in range (i, len(A)):
            if A[j]<min:
                min=A[j]
                minj=j

        A[i],A[minj]=A[minj],A[i]

if __name__ == "__main__":
    A=[3,6,4,1]
    Arry(A)
    print(A)

        
        
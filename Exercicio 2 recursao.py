#Imprimir N em 1 sem loop
def recurssiva(n):
    if n>0:
        print(n)
        recurssiva(n-1)
n=10
recurssiva(n)

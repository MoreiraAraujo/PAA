# Imprima de 1 a n sem usar loops
def recurssiva(n):
    if n>0:
        recurssiva(n-1)
        print(n)
n=10
recurssiva(n)

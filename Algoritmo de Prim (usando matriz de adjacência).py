import sys
def prim(grafo):
    n = len(grafo)
    chave = [sys.maxsize] * n
    pai = [-1] * n  
    visitado = [False] * n
    
    chave[0] = 0 
    
    for _ in range(n):
        
        u = min_key(chave, visitado)
        
        visitado[u] = True  
        
        
        for v in range(n):
            if grafo[u][v] != 0 and not visitado[v] and grafo[u][v] < chave[v]:
                chave[v] = grafo[u][v]
                pai[v] = u
    
    
    print_mst(pai, grafo)


def min_key(chave, visitado):
    min_val = sys.maxsize
    min_index = -1
    
    for v in range(len(chave)):
        if chave[v] < min_val and not visitado[v]:
            min_val = chave[v]
            min_index = v
    
    return min_index


def print_mst(pai, grafo):
    print("Arestas da árvore geradora mínima:")
    for i in range(1, len(grafo)):
        print(f"Vértice {i} - Vértice {pai[i]} com peso {grafo[i][pai[i]]}")


grafo = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(grafo)

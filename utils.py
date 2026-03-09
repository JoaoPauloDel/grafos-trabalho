def calcular_fecho(grafo_original):
    fecho = {v: list(vizinhos) for v, vizinhos in grafo_original.items()}
    n = len(fecho)
    mudou = True
    
    while mudou:
        mudou = False
        vertices = list(fecho.keys())
        for i in range(n):
            for j in range(i + 1, n):
                u, v = vertices[i], vertices[j]
                
                if v not in fecho[u]:
                    if (len(fecho[u]) + len(fecho[v])) >= n:
                        fecho[u].append(v)
                        fecho[v].append(u)
                        mudou = True
    return fecho 
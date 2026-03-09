def verificar_dirac(grafo):
    n = len(grafo)
    if n < 3:
        return False

    for vertice in grafo:
        grau = len(grafo[vertice])
        if grau < n / 2:
            return False
    return True


def verificar_ore(grafo):
    n = len(grafo)
    if n < 3:
        return False

    vertices = list(grafo.keys())

    for i in range(n):
        for j in range(i + 1, n):
            u = vertices[i]
            v = vertices[j]

            if v not in grafo[u]:
                grau_u = len(grafo[u])
                grau_v = len(grafo[v])

                if (grau_u + grau_v) < n:
                    return False
    return True


def verificar_bondy_chvatal(grafo):
    from utils import calcular_fecho

    n = len(grafo)
    fecho = calcular_fecho(grafo)

    for vertice in fecho:
        if len(fecho[vertice]) != n - 1:
            return False
    return True
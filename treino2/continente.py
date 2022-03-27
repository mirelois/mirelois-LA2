'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra.
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si.
A função deverá devolver o tamanho do maior continente.

'''
def bfs_(adj, o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return vis




def maior(vizinhos):
    grafo = dict()
    size = list()
    for fronteira in vizinhos:
        for pais in fronteira:
            if pais not in grafo:
                grafo[pais] = set()
            grafo[pais] |= set(fronteira)
            grafo[pais].remove(pais)

    left = list(set(sum(vizinhos, [])))
    while left:
        pais = left[0]
        vis = bfs_(grafo, pais)
        size.append(len(vis))
        for x in vis:
            left.remove(x)
    return max(size,default=0)


'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em
pareceria com outros autores. O número de Erdos de Paul Erdos é 0.
Para qualquer outro autor, o seu número de Erdos é igual ao menor
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''

def bfs(adj,o):
    dist = {o: 0}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                dist[d] = dist[v] + 1
                vis.add(d)
                queue.append(d)
    return dist


def erdos(artigos, n):
    grafo = {"Paul Erdos" : set()}
    for artigo in artigos:
        for autor in artigos[artigo]:
            if autor not in grafo:
                grafo[autor] = set()
            grafo[autor] |= artigos[artigo]
            grafo[autor].remove(autor)

    erdos = bfs(grafo, "Paul Erdos")

    return sorted(list(filter(lambda a: erdos[a] <= n, erdos.keys())), key=lambda a: (erdos[a], a))
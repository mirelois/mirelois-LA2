def dijkstra(adj, o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist


'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''


def viagem(rotas, origem, destino):
    if origem == destino:
        return 0

    grafo = dict()

    for y, rota in enumerate(rotas):
        for x in range(0, len(rota) - 2, 2):
            peso = rotas[y][x + 1]
            o = rotas[y][x]
            d = rotas[y][x + 2]
            if o not in grafo:
                grafo[o] = dict()
            if d not in grafo:
                grafo[d] = dict()
            pp = grafo[o].get(d, float("inf"))
            if pp > peso:
                grafo[o][d] = peso
                grafo[d][o] = peso
            else:
                grafo[o][d] = pp
                grafo[d][o] = pp

    dist = dijkstra(grafo, origem)

    return dist[destino]
'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade,
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a
letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.

'''

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist


def tamanho(ruas):
    grafo = dict()
    for rua in ruas:
        c1 = rua[0]
        c2 = rua[-1]
        weight = len(rua)
        for c in {c1,c2}:
            if c not in grafo:
                grafo[c] = dict()
        if weight < grafo[c1].get(c2,float("inf")):
            grafo[c1][c2] = weight
            grafo[c2][c1] = weight

    return max([max(list(dict(x).values())) for x in fw(grafo).values()])


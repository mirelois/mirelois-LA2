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


def travessia(mapa):
    x = 0
    y = 0
    grafo = dict()

    for y, line in enumerate(mapa):
        for x, char in enumerate(line):
            v = (x, y)
            if v not in grafo:
                grafo[v] = dict()
            for (nx, ny) in filter(lambda elem: elem[0] < len(line) and elem[1] < len(mapa),
                                   {(abs(e[0]), abs(e[1])) for e in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]}):
                nv = (nx, ny)
                peso = abs(int(mapa[y][x]) - int(mapa[ny][nx]))
                if peso <= 2:
                    if nv not in grafo:
                        grafo[nv] = dict()
                    grafo[v][nv] = peso + 1
                    grafo[nv][v] = peso + 1

    ret = dict()

    for o in range(x + 1):
        dist = dijkstra(grafo, (o, 0))
        # pprint(dist)
        ret[o] = min([dist.get((d, y), float("inf")) for d in range(x + 1)])

    return sorted(ret.items(), key=lambda k: k[1])[0]
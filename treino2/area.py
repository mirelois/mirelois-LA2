'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.

'''

def bfs(adj,o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return len(vis)




def area(p, mapa):

    grafo = {p: set()}

    for y, line in enumerate(mapa):
        for x, char in enumerate(line):
            if char == '*':
                continue

            for (nx, ny) in filter(lambda elem: elem[0] < len(line) and elem[1] < len(mapa), {(abs(e[0]), abs(e[1])) for e in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]}):
                v = (x, y)
                nv = (nx, ny)
                if v not in grafo:
                    grafo[v] = set()
                if mapa[ny][nx] != '*':
                    grafo[v].add(nv)

    return bfs(grafo, p)
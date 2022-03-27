'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''


def bfs(adj, o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def caminho_(adj, o, d):
    pai = bfs(adj, o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0, d)
    return caminho


def caminho(mapa):
    coordmap = {(0, -1): 'O', (0, 1): 'E', (1, 0): 'S', (-1, 0): 'N'}
    adj = {(0, 0): set()}
    x = 0
    y = 0
    max_coord = len(mapa) - 1
    for y, linha in list(enumerate(mapa)):
        for x, char in list(enumerate(linha)):
            for (new_x, new_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if new_x >= 0 and new_y >= 0 and new_y <= max_coord and new_x <= max_coord:
                    if mapa[new_x][new_y] == ' ':
                        if (x, y) not in adj:
                            adj[(x, y)] = set()
                        adj[(x, y)].add((new_x, new_y))

    caminho = caminho_(adj, (0, 0), (x, y))
    res = ""
    limit = len(caminho) - 1
    for i, (x, y) in enumerate(caminho):
        if i + 1 <= limit:
            next_x = caminho[i + 1][0]
            next_y = caminho[i + 1][1]
            res += str(coordmap[(next_x - x, next_y - y)])

    return res


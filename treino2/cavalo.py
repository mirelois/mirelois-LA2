

def saltos(o, d):
    vis = {o}
    queue = [o]
    dist = {o: 0}
    while queue:
        v = queue.pop(0)
        if v == d:
            return dist[v]
        x = v[0]
        y = v[1]
        if x < d[0]:
            i = 1
        if x >= d[0]:
            i = -1
        for nv in [(x + (1 * i), y + 2), (x + (1 * i), y - 2), (x + (2 * i), y + 1), (x + (2 * i), y - 1)]:
            if nv not in vis:
                dist[nv] = dist[v] + 1
                vis.add(nv)
                queue.append(nv)
    return dist[d]
def cruzamentos_V1(ruas):
    ocorrencias = {}
    for rua in ruas:
        for cruzamento in set([rua[0], rua[-1]]):
            if cruzamento not in ocorrencias:
                ocorrencias[cruzamento] = 1
            else:
                ocorrencias[cruzamento] += 1
    return sorted(sorted(list(ocorrencias.items())), key=lambda tuplo: tuplo[1])

def cruzamentos_V2(ruas):
    ocorrencias = dict()
    for rua in ruas:
        for cruzamento in {rua[0], rua[-1]}:
            ocorrencias[cruzamento] = ocorrencias.get(cruzamento, 0) + 1
    return sorted(list(ocorrencias.items()), key=lambda tuplo: (tuplo[1], tuplo[0]))












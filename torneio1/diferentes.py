def aux_numDif(string):
    return len(set(string))


def diferentes(frases):
    frases.sort()
    return sorted(frases, key=aux_numDif, reverse=True)


def diferentes_V2(frases):
    return sorted(sorted(frases), key=lambda x: len(set(x)), reverse=True)


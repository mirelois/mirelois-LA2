def apelidos(nomes):
    return sorted(sorted(nomes),key = lambda nome:len(nome.split())-1)

    
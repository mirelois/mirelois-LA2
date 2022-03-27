def aloca_V1(prefs):
    r = []
    alocados = []
    for aluno in sorted(prefs):
        flag = 0
        for projeto in prefs[aluno]:
            if projeto not in alocados:
                alocados.append(projeto)
                flag = 1
                break
        if flag == 0:
            r.append(aluno)
    return r
            
def aloca_V2(prefs):
    r = list()
    alocados = list()
    for aluno in sorted(prefs):
        for projeto in prefs[aluno]:
            if projeto not in alocados:
                alocados.append(projeto)
                break
        else:
            r.append(aluno)
    return r
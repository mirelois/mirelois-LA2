def formula1_v1(log):
    log.sort()
    timelist = []
    tempos = dict()
    return_list = list()
    for (tempo, piloto) in log:
        if piloto not in tempos:
            tempos[piloto] = []
        tempos[piloto].append(tempo-sum(tempos[piloto]))
    for piloto in tempos:
        timelist += tempos[piloto]
    min_ = min(timelist, default=0)
    for piloto in tempos:
        if min(tempos[piloto]) == min_:
            return_list.append(piloto)
    return sorted(return_list)

def formula1_v2(log):
    log.sort()
    tempos = dict()
    for (tempo, piloto) in log:
        if piloto not in tempos:
            tempos[piloto] = [tempo, 0]
        total = tempos[piloto][1]
        min_ = tempos[piloto][0]
        if min_ > tempo-total:
            min_ = tempo-total
        tempos[piloto] = [min_, tempo]
    min_total = min([tempos[key][0] for key in tempos], default = 0)
    return list(filter(lambda x: tempos[x][0] == min_total, sorted(tempos)))

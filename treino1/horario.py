def meio(x, inte):
    return x > inte[0] and x < inte[1]

#funçao que recebe um par de horas e uma lista com pares de horas
#verifica se existe crossover entre o intervalo dado pelo par e os intervalos em dias
def checkHora(hora_par, dia):
    r = True
    for (hi, hf) in dia:
        for h in [hora_par[0], hora_par[1]]:
            if meio(h, (hi, hf)):
                r = False
        for h in [hi, hf]:
            if meio(h, hora_par):
                r = False

    return r

#calcula as horas semanais a partir de um dict
def horaTotal(horario):
    total = 0
    for dia in horario:
        for (hi, hf) in horario[dia]:
            total += hf - hi
    return total


def horario(ucs, alunos):
    r = list()
    for aluno in alunos:
        table = dict()
        fail = True
        for uc in alunos[aluno]:
            if uc not in ucs:
                fail = False
            else:
                dia = ucs[uc][0]
                horai = ucs[uc][1]
                horaf = horai + ucs[uc][2]
                if dia in table:
                    if checkHora((horai, horaf), table[dia]):
                        table[dia].append((horai, horaf))
                    else:
                        fail = False
                else:
                    table[dia] = [(horai, horaf)]
        if fail == True:
            r.append((aluno, horaTotal(table)))

    return sorted(r,key = lambda x: (-x[1], x[0]))
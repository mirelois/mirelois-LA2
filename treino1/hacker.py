def hacker(log):
    dic = dict()

    for num,email in log:
        cont = 0
        if email not in dic:
            dic[email] = list(num)
            continue
        for ind in range(len(num)):
            if num[ind] != '*':
                dic[email][ind] = num[ind]

    return sorted(sorted([("".join(y), x) for (x, y) in list(dic.items())], key = lambda x: x[1]), key = lambda t: dic[t[1]].count('*'))

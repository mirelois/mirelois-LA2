def robot_V1(comandos):
    d = [0,1] #vetor de direçao
    max_min = [0,0,0,0] # [min x , min y, max x, max y]
    r = list() # return
    coords = [0,0]# current coordenates
    for comando in comandos:
        if comando == 'E':
            d = [-d[1], d[0]] # x' = x.cos(t) - y.sin(t) ; y' = x.sin(t) + y.cos(t) t = 90
        elif comando == 'D':
            d = [d[1], -d[0]]# x' = x.cos(t) - y.sin(t) ; y' = x.sin(t) + y.cos(t) t = -90
        elif comando == 'A': 
            coords = list(map(lambda x,y: x+y, coords, d)) # coords + d
            max_min = [min(coords[0],max_min[0]), min(coords[1],max_min[1]), max(coords[0],max_min[2]), max(coords[1],max_min[3])] # atualizaçao do max_min
        elif comando == 'H':
            r.append(tuple(max_min))#adicionar retangulo a r
            max_min= [0,0,0,0]
            coords = [0,0]
            d = [0,1]#reset the robot
    return r
    
    
    
def robot_V2(comandos):
    d = [0,1] #vetor de direçao
    x = [0] #posiçoes x
    y = [0] #posiçoes y
    r = list() # return
    for comando in comandos:
        if comando == 'E':
            d = [-d[1], d[0]] # x' = x.cos(t) - y.sin(t) ; y' = x.sin(t) + y.cos(t) t = 90
        elif comando == 'D':
            d = [d[1], -d[0]]# x' = x.cos(t) - y.sin(t) ; y' = x.sin(t) + y.cos(t) t = -90
        elif comando == 'A': 
            x.append(x[-1] + d[0])#new x 
            y.append(y[-1] + d[1])#new y
        elif comando == 'H':
            r.append((min(x), min(y), max(x), max(y)))#adicionar retangulo a r
            x = [0]#reset x
            y = [0]# reset y
            d = [0,1]#reset direction of the robot
    return r
      
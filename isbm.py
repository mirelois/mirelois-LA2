def isbn_V1(livros):
    r = list()
    for livro in livros:
        if sum(map(lambda x,y: x*y , [1,3]*7 , [int(x) for x in livros[livro]])) % 10 != 0:
            r.append(livro)
    return r

def isbn_V2(livros): 
    return list(filter(lambda n: sum(map(lambda x,y: x*y , [1,3]*7 , [int(x) for x in livros[n]]))%10 != 0, sorted(livros)))
    










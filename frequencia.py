def frequencia(texto):
    freq = dict()
    for word in texto.split():
        freq[word] = freq.get(word, 0) + 1
    return list(sorted(sorted(freq), key=lambda val: freq[val], reverse=True))





















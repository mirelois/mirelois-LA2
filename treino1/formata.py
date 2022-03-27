def formata(codigo):
    ret = str()
    spaces = str()
    ignore = False
    for char in codigo:
        if ignore and char == ' ':
            continue
        ignore = False
        if char == ';':
            ignore = True
            ret += char + '\n' + spaces
        elif char == '{':
            ignore = True
            spaces += '  '
            ret += char + '\n' + spaces
        elif char == '}':
            ignore = True
            spaces = spaces[:-2]
            ret = ret[:-2]
            ret += char + '\n' + spaces
        else:
            ret += char
    return ret.rstrip()
def recursiveS(L, e):
    if L[0] == e:
        return True
    elif len(L) == 0:
        return False
    else:
        return recursiveS(L[1:], e)

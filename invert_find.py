espace = [[[[[1], 1], 5, [[2]]], 3], 4]

def invert_find(espace, coordonnee, lancee):
    if len(coordonnee) == 1:
        return espace
    if lancee:
        coordonnee.pop(0)
    return invert_find(espace[coordonnee[0]], coordonnee, True)

print(invert_find(espace, [0, 1], False))

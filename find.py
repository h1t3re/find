espace = [[[[[1], 1], 5, [[2]]], 3], 4]

def find(espace, item, coordonnee):
    for dimension in espace:
        if dimension == item:
            coordonnee.append(espace.index(dimension))
            yield coordonnee
        else:
            if isinstance(dimension, list):
                for x in find(dimension, item, coordonnee):
                    x.append(espace.index(dimension))
                    yield x
                    coordonnee = []

print("espace = ", end="")
print(espace, end="\n")
for i in range(1, 6):
    for x in find(espace, i, []):
        print("coordonnee de "+str(i)+" = ", end="")
        print(x[::-1], end="\n")

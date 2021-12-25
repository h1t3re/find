espace = [[[[[1], 1], 5, [[2]]], 3], 4]

def find(espace, item, coordonnee):
    for dimension in espace:
        if dimension == item:
            coordonnee.append(espace.index(dimension))
            yield coordonnee
        else:
            if isinstance(dimension, list):
                for x in find(dimension, item, coordonnee):
                    coordonnee = list(x)
                    coordonnee.append(espace.index(dimension))
                    yield coordonnee
                    coordonnee = []

print(espace)
print("\n")
for i in range(1, 6):
    print("coordonnee de "+str(i) + " = ", end="")
    for x in find(espace, i, []):
        print(x)
    print("\n")

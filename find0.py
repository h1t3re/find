espace = [[[[[1], 1], 5, [[2]]], 3], 4]

def exec_function(func=None, *iterable):
    arg0, *args = iterable
    for x in arg0:
        yield func(x, *args)

def find(dimension=[], espace=[], item=0, coordonnee=[]):
    if dimension == item:
        coordonnee.append(espace.index(dimension))
        yield coordonnee
    if type(dimension) is list:
        for x in exec_function(find, dimension, dimension, item, coordonnee):
            for y in x:
                if espace != dimension:
                    coordonnee.append(espace.index(dimension))
                yield coordonnee
                coordonnee = []
print(espace)
for i in range(1, 6):
    for x in find(espace, espace, i, []):
        print(x, end="\n")

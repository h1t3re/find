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

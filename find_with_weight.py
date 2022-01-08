espace = (((2,2), 1), ((2,7), 1),(((2, 9), 5), 2), 1)

def find_with_weight(espace, item, weight):
    weight = weight+espace[len(espace)-1]
    for dimension in espace[:-1]:
        if dimension == item:
            yield (dimension, weight)
        else:   
            if type(dimension) == tuple:
                for x in find_with_weight(dimension, item, weight):
                    yield x

for x in find_with_weight(espace, 2, 0):
    print(x)

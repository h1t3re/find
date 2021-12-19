def find(espace0, item, args):
    for x in espace0:
        if x == item:
            args.append(espace0.index(x))
            yield args
        else:
            if isinstance(x, list):
                for z in find(x, item, args):
                    args = list(z)
                    args.append(espace0.index(x))
                    yield args[::-1]

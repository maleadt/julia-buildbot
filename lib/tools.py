# TODO: merging PATH env var shouldn't use space as separator
def merge(*dicts):
    keys = set().union(*dicts)

    merged = {}
    for k in keys:
        values = []
        for dic in dicts:
            if k in dic:
                values.append(dic[k])
        if len(values) == 1:
            merged[k] = values[0]
        else:
            merged[k] = " ".join(values)

    return merged

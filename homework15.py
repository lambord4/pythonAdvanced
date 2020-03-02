def find_common_keys(dict1, dict2):
    dicts = [dict1, dict2]

    common_keys = set(dict1.keys())

    for d in dicts[1:]:
        common_keys.intersection_update(set(d.keys()))
    print(common_keys)

    return common_keys


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 7, 'd': 5}

find_common_keys(d1, d2)

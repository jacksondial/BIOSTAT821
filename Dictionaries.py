chromosomes = [1, 2, 3, 3, 2, 4, 4, 2]


def dedup(chromosomes):
    my_dict = dict()
    for chromo in chromosomes:
        my_dict[chromo] = True
    dedup = list(my_dict.keys())
    return dedup


dedup(chromosomes)

# Patrick's example

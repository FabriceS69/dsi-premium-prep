''' Deduping '''
lst = ['hockey', 'basketball', 'hockey', 'sportsball', 'deathball', 'skiing', 'javelin', 'javelin']
# lst = list(set(lst)) # ['sportsball', 'hockey', 'deathball', 'basketball']

# print(lst)

def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

# print(lst)
# print(dedupe_in_order(lst))


def star_args(*args):
    print(type(args))
    for item in args:
        print(item)
    return None

# star_args('cat', 72.4, [[1,2,3], 'bird'], False)



a = ['rabbit', 'cat', 'dog', 'leech', 'kangaroo', 'squirrel']
b = ['eagle', 'shark', 'cat', 'leech', 'caracol']
c = ['rabbit', 'eagle', 'cat', 'platypus', 'nutria', 'manatee']

def union(lst_1, lst_2):
    set_union = lst_1.copy()
    
    for element in lst_2:
        if element not in set_union:
            set_union.append(element)
    return set_union

# print(union(a, b))



def union_mult_sets(*mult_sets):
    set_union = []

    for lst in mult_sets:
        for item in lst:
            if item not in set_union:
                set_union.append(item)

    return set_union

# print(union_mult_sets(a, b, c))


def intersection(lst_1, lst_2):
    set_intersect = []
     
    for element in lst_1:
        if element in lst_2:
            set_intersect.append(element)

    return set_intersect

# print(intersection(a, b))


def intersection_mult_sets(*mult_sets):
    set_intersect = []

    if len(mult_sets) > 1 and len(mult_sets[0]) > 0:
        for element in mult_sets[0]:
            is_member = True

            for set_ in mult_sets[1:]:
                if element not in set_:
                    is_member = False
                    break

            if is_member:
                set_intersect.append(element)
    return set_intersect

# print(intersection_mult_sets(a, b, c))


def difference(lst_1, lst_2):
    set_difference = []

    for element in lst_1:
        if element not in lst_2:
            set_difference.append(element)
    return set_difference

# print(difference(a, b))
# print(difference(a, intersection(a, b)))

a = ['rabbit', 'cat', 'dog', 'leech', 'kangaroo', 'squirrel']
b = ['eagle', 'shark', 'cat', 'leech', 'caracol']
c = ['rabbit', 'eagle', 'cat', 'platypus', 'nutria', 'manatee']

sample_space = union_mult_sets(a, b, c, ['albatross', 'vole'])


def complement(sample_space, lst):
    return difference(sample_space, lst)

# print(complement(sample_space, union(a, b)))
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





a = ['rabbit', 'cat', 'dog', 'leech', 'kangaroo', 'squirrel']
b = ['eagle', 'shark', 'cat', 'leech', 'caracol']
c = ['rabbit', 'eagle', 'cat', 'platypus', 'nutria', 'manatee']

def union(lst_1, lst_2):
    set_union = lst_1.copy()
    
    for element in lst_2:
        if element not in set_union:
            set_union.append(element)
    return set_union

print(union(a, b))
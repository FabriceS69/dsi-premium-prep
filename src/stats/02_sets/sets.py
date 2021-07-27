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




def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod

# print(1 / factorial(10))


def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

def permutations(n, k):
    perm = 1
    for i in range(n-k, n+1):
    # for i in range((n-k)+1, n+1):
        perm *= i
    return perm

# print(permutations(10, 4))




base_5 = ['scientist', 'lawyer', 'doctor', 'astronaut', 'firefighter']

counting = []

for p1 in base_5:
    for p2 in base_5:
        for p3 in base_5:
            for p4 in base_5:
                for p5 in base_5:
                    counting.append([p1, p2, p3, p4, p5])

# for p_num in counting:
#     print(p_num)

perms = []

for p_num in counting:
    perm = True

    for p in p_num:
        if p_num.count(p) > 1:
            perm = False
            break
    
    if perm == True:
        perms.append(p_num)

# for p_num in perms:
#     print(p_num)



def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_ 

# test_list = ['a', 'b', 'c', 'd']
# print(swap(test_list, 1, 2))

def heaps_non_recursive(lst, k):
    lst_copy = lst.copy()

    # holds stack state
    c = [0] * len(lst)

    perms = [lst_copy[:k]]

    i = 0 # acts like a pointer to c
    while i < len(lst_copy):

        input(lst_copy)

        if c[i] < i:
            if i % 2 == 0:
                lst_copy = swap(lst_copy, 0, i)
            else:
                lst_copy = swap(lst_copy, c[i], i)

            if lst_copy[:k] not in perms:
                perms.append(lst_copy[:k])

            # incr the counters
            c[i] += 1

            # reset i
            i = 0
        else:
            #reset counter state
            c[i] = 0
            i += 1
    return perms



base_5 = ['scientist', 'lawyer', 'doctor', 'astronaut', 'firefighter']


# heaps = heaps_non_recursive(base_5, 5)

# for perm in heaps:
#     print(perm)


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def combinations(n, k):
    return int(permutations(n, k) / factorial(k))

def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# print(combinations(52, 5)) # 2598960






# An expensive counting approach
num_combs = combinations(11, 5)
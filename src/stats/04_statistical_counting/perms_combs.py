
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

def basketball_combs():
    eleven_nums = range(1, 21+1)

    # every arrangement of 5
    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i, j, k, l, m])
    perms = []

    for five in possible_five:
        if len(list(set(five))) == 5:
            perms.append(five)

    # for five in perms:
    #     print(five)

    combs = []

    for five in perms:
        sorted_five = sorted(five)

        if sorted_five not in combs:
            print(sorted_five)
            combs.append(sorted_five)

    return combs

# bask_combs = basketball_combs()

# for comb in bask_combs:
#     print(comb)


# an expensive Sampling approach

from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []

    player_range = range(1, team_size+1)

    while len(combs) < combinations(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)

            if player_num not in player_comb:
                player_comb.append(player_num)
        
        player_comb = sorted(player_comb)

        if player_comb not in combs:
            print(player_comb)
            combs.append(player_comb)
    return combs


combs_samp = basketball_combs_samp(team_size=21, num_players=5)
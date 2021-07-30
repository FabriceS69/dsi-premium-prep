
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

test_list = ['a', 'b', 'c', 'd']

print(swap(test_list, 0, 2))
def mean(lst, trim=0):
    lst_ = lst.copy()
    
    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]

    return sum(lst) / len(lst)

a = [1,2,3,4,5, 5000]

print(mean(a, trim=1))
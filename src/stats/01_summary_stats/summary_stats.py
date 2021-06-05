def mean(lst, trim_by=0):
    lst_ = lst.copy()
    
    if trim_by > 0:
        lst_ = sorted(lst_)[trim_by: -trim_by]
    
    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim_by=1))


urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# print(f'Sample Mean Urban: {round(mean(urban), 1)}')
# print(f'Sample Mean Farmhouse: {round(mean(farmhouse), 1)}')

# print()

# print(f'Trimmed Sample Mean Urban: {round(mean(urban, trim_by=1), 1)}')
# print(f'Trimmed Sample Mean Farmhouse: {round(mean(farmhouse, trim_by=1), 1)}')



def median(lst):
    lst_ = sorted(lst)

    if len(lst) % 2:
        mid_idx = int(len(lst) / 2)
        return lst_[mid_idx]
    else:
        upper_mid_idx = int(len(lst) / 2)
        return mean([lst_[upper_mid_idx-1], lst_[upper_mid_idx]])



odd_list = [13, 18, 13, 15, 13, 16, 14, 21, 13]
even_list = [15, 14, 10, 8, 12, 8, 16, 13]

# print(sorted(odd_list))
# print(median(odd_list))
# print()
# print(sorted(even_list))
# print(median(even_list))


urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0]

# print(sorted(urban))
# print(f'Sample median Urban: {round(median(urban), 1)}')

# print()
# print(sorted(farmhouse))
# print(f'Sample median Farmhouse: {round(median(farmhouse), 1)}')


home_sales = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]
# print(sorted(home_sales))
# print(f'mean of home sales: {round(mean(home_sales))}')
# print(f'median of home sales: {round(median(home_sales))}')



pets = ['hermit crab', 'cat', 'dog', 'goldfish', 'ferret', 'ferret',  'cat', 'cat', 'ferret',] * 5

# print(pets.count('ferret'))

def mode(lst):
    most_occurring = lst[0]

    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item
    
    return most_occurring

print(mode(pets))
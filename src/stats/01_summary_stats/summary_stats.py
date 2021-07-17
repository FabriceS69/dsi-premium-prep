def mean(lst, trim=0):
    lst_ = lst.copy()
    
    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]

    return sum(lst_) / len(lst_)

a = [1,2,3,4,5, 5000]

# print(mean(a, trim=1))




urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

'''
A. Determine the sample mean for each group.
'''
# print(sorted(urban))
# print(f'Sample Mean for Urban: {round(mean(urban), 1)}')
# print()
# print(sorted(farmhouse))
# print(f'Sample Mean for Farmhouse: {round(mean(farmhouse), 1)}')


'''
B. Determine the trimmed mean for each group by trimming the smallest and largest value 
from each group.
'''
# print(sorted(urban))
# print(f'Sample Trimmed Mean for Urban: {round(mean(urban, trim=1), 1)}')
# print()
# print(sorted(farmhouse))
# print(f'Sample Trimmed Mean for Farmhouse: {round(mean(farmhouse, trim=1), 1)}')



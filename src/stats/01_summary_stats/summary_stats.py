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
# print()

'''
B. Determine the trimmed mean for each group by trimming the smallest and largest value 
from each group.
'''
# print(sorted(urban))
# print(f'Sample Trimmed Mean for Urban: {round(mean(urban, trim=1), 1)}')
# print()
# print(sorted(farmhouse))
# print(f'Sample Trimmed Mean for Farmhouse: {round(mean(farmhouse, trim=1), 1)}')


def median(lst):
    lst_sorted = sorted(lst)

    if len(lst) % 2 == 1:
        mid = int(len(lst) / 2)
        return lst_sorted[mid]
    else:
        upper_mid = int(len(lst) / 2)
        return (lst_sorted[upper_mid] + lst_sorted[upper_mid-1]) / 2

odd_list = [13, 18, 13, 14, 13, 16, 14, 21, 13]
even_list = [15, 14, 10, 8, 12, 8, 16, 13]

# print(median(odd_list))
# print(median(even_list))


urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0]

# print(sorted(urban))
# print(f'Median for Urban: {round(median(urban), 1)}')
# print()
# print(sorted(farmhouse))
# print(f'Median for Farmhouse: {round(median(farmhouse), 1)}')


interests = ['cats', 'skateboarding', 'music', 'music', 'kayaking', 'darts', 'darts', 'music', 'frogs', 'darts']

def mode(lst):
    most_freq = lst[0]

    for item in lst[1:]:
        if lst.count(item) >= lst.count(most_freq):
            most_freq = item
    return most_freq

# print(mode(interests))



from random import choice

def get_samps(sample_range, num_samples=5):
    samples = []

    for _ in range(num_samples):
        samples.append(choice(sample_range))
    return samples

num_samples = 100
sample_range = list(range(0, 99+1))
# print(f'mu: {mean(sample_range)}')
# print()
# means = []
# for _ in range(100000):
#     means.append(mean(get_samps(sample_range, num_samples)))

# print(f'list of x_bar: {means}')
# print(f'mean of means: {mean(means)}')




def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)    
    sorted_list = sorted(lst)
    # print(sorted_list)
    if len(lst) % 2 == 1:
        lower_half = sorted_list[0: int(len(lst) / 2)+1]
        # print(lower_half)
        upper_half = sorted_list[int(len(lst) / 2):]
        # print(upper_half)
    else:
        lower_half = sorted_list[0: int(len(lst) / 2)]
        # print(lower_half)
        upper_half = sorted_list[int(len(lst) / 2):]
        # print(upper_half)
    q1 = median(lower_half)
    q3 = median(upper_half)
    return min_, q1, med, q3, max_

# lst = list(range(0,51,5))
# print(five_number_summary(lst))


a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]

# print('a:')
# print(mean(a))
# print(five_number_summary(a))
# print()
# print('b:')
# print(mean(b))
# print(five_number_summary(b))



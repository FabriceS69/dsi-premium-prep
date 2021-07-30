pets = ['C', 'D', 'F', 'G']

outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                outcomes.append([pet1, pet2, pet3, pet4])

# for pet_outcome in outcomes:
#     print(pet_outcome)

# print(len(outcomes))
# print(4**4)

two_or_more_cats = []

for outcome in outcomes:
    if outcome.count('C') >= 2:
        two_or_more_cats.append(outcome)

# print(len(two_or_more_cats) / len(outcomes))



from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

# print(series_of_flips(10))

num_trials = 1000

# proba_estimations = []

# for _ in range(1000):
#     eight_heads = 0

#     for _ in range(num_trials):
#         res = series_of_flips(10)
#         if res.count('H') == 8:
#             eight_heads += 1


#     proba_estimations.append(eight_heads / num_trials)


# print(proba_estimations)
# print(sum(proba_estimations) / 1000)
# print(min(proba_estimations), ' ', max(proba_estimations))



def four_flip_sample_space():
    four_flips = []
    
    for flip1 in ['T', 'H']:
        for flip2 in ['T', 'H']:
            for flip3 in ['T', 'H']:
                for flip4 in ['T', 'H']:
                    four_flips.append([flip1, flip2, flip3, flip4])
    return four_flips

# for outcome in four_flip_sample_space():
#     print(outcome)

outcomes = four_flip_sample_space()

three_heads = []

# for outcome in outcomes:
#     if outcome.count('H') == 3:
#         three_heads.append(outcome)

# print(len(three_heads) / len(outcomes))




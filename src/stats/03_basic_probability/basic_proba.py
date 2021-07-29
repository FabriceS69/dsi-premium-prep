pets = ['C', 'D', 'F', 'G']

outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                outcomes.append([pet1, pet2, pet3, pet4])

for pet_outcome in outcomes:
    print(pet_outcome)
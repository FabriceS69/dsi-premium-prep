rolls = range(1, 36+1)

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
card_nums = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Jack', 'Queen', 'King']

cards = []
for suit in suits:
    for card in card_nums:
        cards.append(f'{card} of {suit}')

# for card in cards:
#     print(card)

coin_flips = []
for f1 in ['T', 'H']:
    for f2 in ['T', 'H']:
        for f3 in ['T', 'H']:
            coin_flips.append([f1, f2, f3])

S = []
for roll in rolls:
    for card in cards:
        for flip in coin_flips:
            S.append([roll, card, flip])

# print(len(S))



# for outcome in S:
#     print(outcome)


hits = []
range_to_hit = 18
two_heads = []

for outcome in S:
    if outcome[2].count('H') == 2:
        two_heads.append(outcome)

    if outcome[0] >= range_to_hit:
        if outcome[2].count('H') == 2:
            hits.append(outcome)

print(18/36)
print(round(len(two_heads)/len(S), 3))
print(round(len(hits) / len(S), 3))
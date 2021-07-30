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



for outcome in S:
    print(outcome)
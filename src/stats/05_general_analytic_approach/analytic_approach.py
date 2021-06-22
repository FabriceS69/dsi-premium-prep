rolls = range(1, 36+1)

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
card_nums = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

cards = []
for suit in suits:
    for card in card_nums:
        cards.append(f'{card} of {suit}')

for card in cards:
    print(card)
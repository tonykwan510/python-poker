"""Play a simple card game.

A simple card games in which players take turns to draw cards.
The player with highest total card score wins.
Card score = Suit score * Rank score
Suit score: Spades = 1, Diamonds = 2, Hearts = 3, Clubs = 4
Rank score: A = 1, 2 = 2, ..., 10 = 10, J = 11, Q = 12, K = 13
"""
from poker import CardDeck

players = 2
cards = 3

suit_scores = {'Spades': 1, 'Diamonds': 2, 'Hearts': 3, 'Clubs': 4}
rank_scores = {str(_): _ for _ in range(2, 11)}
rank_scores.update({'A': 1, 'J': 11, 'Q': 12, 'K': 13})
card_score = lambda card: suit_scores[card.suit()] * rank_scores[card.rank()]

deck = CardDeck()
deck.shuffle()

hands = [[] for _ in range(players)]
for i in range(cards):
    for j in range(players):
        hands[j].append(deck.draw())

winners = []
score_max = 0
for i, hand in enumerate(hands, 1):
    score = sum(card_score(card) for card in hand)

    if score > score_max:
        winners = [i]
        score_max = score
    elif score == score_max:
        winners.append(i)

    print('Player', i)
    print('  Cards:', *hand)
    print('  Score:', score)

print('Winner: Player', *winners)

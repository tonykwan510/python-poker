# Python Poker

A Python module for poker game development.

## Requirements

The following modules from the Python standard library are used.
- `functools`
- `random`
- `typing`

## Examples

### Example 1

The following script draws from a standard deck until we get all 4 suits. Then sort the cards.
```python
from poker import CardDeck

deck = CardDeck()
deck.shuffle()
cards = []
suits = set()

while len(suits) < 4:
    card = deck.draw()
    cards.append(card)
    suits.add(card.suit())

cards.sort()
print(*cards)
```
Sample output:
```
♠5  ♠9  ♠10 ♦2  ♦7  ♦9  ♦J  ♦K  ♥4  ♣4  ♣Q  ♣A
```

### Example 2

The following script plays a sample game with 2 players each drawing 3 cards. The winner is the one with higher *total card score*.
```python
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
```
Sample output:
```
Player 1
  Cards: ♣8  ♦7  ♣10
  Score: 86
Player 2
  Cards: ♠6  ♦6  ♠5
  Score: 23
Winner: Player 1
```
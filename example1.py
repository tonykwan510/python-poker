"""Draw from a standard deck until we get all 4 suits. Then sort the cards."""
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

"""Poker card module."""
from typing import Sequence
from functools import total_ordering
from random import randrange

SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
SUIT_SYMBOLS = {
    'Spades': u'\N{black spade suit}',
    'Diamonds': u'\N{black diamond suit}',
    'Hearts': u'\N{black heart suit}',
    'Clubs': u'\N{black club suit}',
}
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

@total_ordering
class Card:
    """Poker card class."""

    def __init__(self, suit: str, rank: str) -> None:
        """Inits Card with suit and rank.

        Raises:
          ValueError: Unknown suit or rank.
        """

        try:
            self._suit = SUITS.index(suit)
        except ValueError:
            raise ValueError(f'Unknown suit: {suit}.') from None

        try:
            self._rank = RANKS.index(rank)
        except ValueError:
            raise ValueError(f'Unknown rank: {rank}.') from None

    def __hash__(self) -> int:
        return hash((self._suit, self._rank))

    def __str__(self) -> str:
        suit = SUITS[self._suit]
        return '{}{:2}'.format(SUIT_SYMBOLS[suit], RANKS[self._rank])

    def __eq__(self, other: 'Card') -> bool:
        return self._suit == other._suit and self._rank == other._rank

    def __lt__(self, other: 'Card') -> bool:
        """Ordering of cards by suit and rank.

        Suit order: Spades < Diamonds < Hearts < Clubs
        Rank order: 2 < ... < 10 < J < Q < K < A
        """
        return (self._suit, self._rank) < (other._suit, other._rank)

    def suit(self) -> str:
        """Returns suit of card."""
        return SUITS[self._suit]

    def rank(self) -> str:
        """Returns rank of card."""
        return RANKS[self._rank]

class CardDeck:
    """Card deck class.

    Attributes:
      card_set: Maximal set of cards in the deck.
      cards: List of cards in current deck.
    """

    def __init__(self, cards: Sequence[Card] = None) -> None:
        """Inits CardDeck with a set of cards.

        Raises:
          TypeError: Input is not a sequence of cards.
          IndexError: Input is an empty sequence.
        """

        if cards is None:
            self.card_set = set(Card(suit, rank)
                                for suit in SUITS for rank in RANKS)
        elif not isinstance(cards, Sequence):
            raise TypeError('Input is not a sequence of cards.')
        elif not all(isinstance(card, Card) for card in cards):
            raise TypeError('Input is not a sequence of cards.')
        elif len(cards) == 0:
            raise IndexError('Input is an empty sequence.')
        else:
            self.card_set = set(cards)

        self.reset()

    def reset(self) -> None:
        """Reset the deck to original."""
        self.cards = list(self.card_set)

    def __len__(self) -> int:
        """Returns the current number of cards in the deck."""
        return len(self.cards)

    def add(self, card: Card) -> bool:
        """Add a card to the deck.

        Add a card to the deck if the card is:
        1. Among the original cards; and
        2. Not already in the deck.

        Potential uses:
          Re-use discarded cards when the draw pile is empty.

        Returns:
          A boolean indicating whether the card is added.
        """

        if card in self.card_set and card not in self.cards:
            self.cards.append(card)
            return True
        else:
            return False

    def draw(self) -> Card:
        """Draw a card from the top of the deck.

        Raises:
          IndexError: The deck is empty.
        """
        try:
            return self.cards.pop()
        except IndexError:
            raise IndexError('card deck is empty') from None

    def shuffle(self) -> None:
        """Shuffle the deck."""
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = randrange(n_cards)
            if i != j:
                self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

if __name__ == '__main__':
    deck = CardDeck()
    deck.shuffle()
    cards = [deck.draw() for _ in range(10)]
    cards.sort()
    print(*cards)

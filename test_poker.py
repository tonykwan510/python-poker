"""Unit test for poker module."""
import unittest
from poker import Card, CardDeck

class TestCard(unittest.TestCase):
    """Unit test for Card."""

    def testInit_InvalidSuit(self):
        with self.assertRaises(ValueError):
            Card('Spade', 'A')

    def testInit_InvalidRank(self):
        with self.assertRaises(ValueError):
            Card('Spades', '1')

    def testEq(self):
        self.assertEqual(Card('Spades', 'A'), Card('Spades', 'A'))
        self.assertNotEqual(Card('Spades', 'A'), Card('Spades', '2'))
        self.assertNotEqual(Card('Spades', 'A'), Card('Diamonds', '2'))

    def testLt(self):
        self.assertLess(Card('Spades', 'A'), Card('Diamonds', 'A'))
        self.assertLess(Card('Diamonds', 'A'), Card('Hearts', 'A'))
        self.assertLess(Card('Hearts', 'A'), Card('Clubs', 'A'))
        self.assertLess(Card('Spades', '2'), Card('Spades', 'A'))

    def testSuit(self):
        card = Card('Spades', 'A')
        self.assertEqual(card.suit(), 'Spades')

    def testRank(self):
        card = Card('Spades', 'A')
        self.assertEqual(card.rank(), 'A')

class TestCardDeck(unittest.TestCase):
    """Unit test for CardDeck."""
    DEFAULT_DECK_SIZE = 52

    def testInit_InvalidCards(self):
        card = Card('Spades', 'A')
        with self.assertRaises(TypeError):
            CardDeck(card)
        with self.assertRaises(TypeError):
            CardDeck([1])
        with self.assertRaises(IndexError):
            CardDeck([])

    def testInit_DefaultCards(self):
        deck = CardDeck()
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE)

    def testInit_Cards(self):
        cards = [Card('Spades', 'A'), Card('Spades', '2')]
        deck = CardDeck(cards)
        self.assertEqual(len(deck), 2)

    def testInit_DuplicateCards(self):
        cards = [Card('Spades', 'A'), Card('Spades', 'A')]
        deck = CardDeck(cards)
        self.assertEqual(len(deck), 1)

    def testDraw_DeckSize(self):
        deck = CardDeck()
        deck.draw()
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE - 1)

    def testDraw_EmptyDeck(self):
        deck = CardDeck()
        while len(deck) > 0:
            deck.draw()
        with self.assertRaises(IndexError):
            deck.draw()

    def testAdd_DeckSize(self):
        deck = CardDeck()
        card = deck.draw()
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE - 1)
        res = deck.add(card)
        self.assertTrue(res)
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE)

    def testAdd_DuplicateCards(self):
        cards = [Card('Spades', 'A')]
        deck = CardDeck(cards)
        self.assertEqual(len(deck), 1)
        res = deck.add(cards[0])
        self.assertFalse(res)
        self.assertEqual(len(deck), 1)

    def testAdd_InvalidCard(self):
        cards = [Card('Spades', 'A'), Card('Spades', '2')]
        deck = CardDeck(cards)
        res = deck.add(Card('Spades', '3'))
        self.assertFalse(res)
        self.assertEqual(len(deck), 2)

    def testReset(self):
        deck = CardDeck()
        deck.draw()
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE - 1)
        deck.reset()
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE)

    def testShuffle_DeckSize(self):
        deck = CardDeck()
        deck.shuffle()
        self.assertEqual(len(deck), self.DEFAULT_DECK_SIZE)

    def testShuffle_DuplicateCards(self):
        deck = CardDeck()
        deck.shuffle()
        self.assertEqual(len(deck), len(set(deck.cards)))

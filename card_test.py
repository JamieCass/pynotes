import unittest
from cards_final import Card, Deck


class CardTests(unittest.TestCase):

    def setUp(self):
        self.card = Card('A', 'Spades')

    def test_init(self):
        """Each card should have a suit and a value"""
        self.assertEqual(self.card.suit, 'Spades')
        self.assertEqual(self.card.value, 'A')

    def test_repr(self):
        """Should return a f string with the VALUE folowed by the SUIT"""
        self.assertEqual(repr(self.card),'A of Spades')

class DeckTests(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """init should have a list of 52 cards with values and suits"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(self.deck.count(), 52)

    def test_repr(self):
        """Should return a f string with how many cards are in the deck"""
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        """count should tell how many cards are in the deck, and change everytime cards are dealt"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop() #we take a card away and make sure count will display 1 card less when its called on.
        self.assertEqual(self.deck.count(), 51) # now the deck should have 1 less card in than before.

    def test_deal_sufficent_cards(self):
        """_deal should deal the amount of cards required, as long as there are enough cards left in the deck"""
        cards = self.deck._deal(10) # deal 10 cards
        self.assertEqual(len(cards), 10) # check to see if the length of cards dealt matches the the number stated (10)
        self.assertEqual(self.deck.count(), 42) # check the deck now has '10' cards less than before

    def test_deal_insufficent_cards(self):
        """_deal should only deal however many cards are in the deck"""
        cards = self.deck._deal(57) # try and deal 57 cards
        self.assertEqual(len(cards), 52) # Check to see if the fresh deck is 52 cards and therefore will only deal 52 cards in the hand.
        self.assertEqual(self.deck.count(), 0) # the deck will now have no cards left.

    def test_deal_no_cards(self):
        """_deal should come up with an error message if there are not cards in the deck"""
        self.deck._deal(self.deck.count())# dealing the count of cards in the deck (the wont be anly left aftet this line.)
        with self.assertRaises(ValueError):
            self.deck._deal(1) # try and deal 1 more card after we have dealt the rest of the deck. it will raise an error.

    def test_deal_card(self):
        """deal card should only deal 1 card at a time"""
        card = self.deck.cards[-1] # take a card out of the deck
        dealt_card = self.deck.deal_card() # call the _deal function
        self.assertEqual(card, dealt_card) # make sure the 'dealt_card' and the 'card' are the same
        self.assertEqual(self.deck.count(), 51) # make sure there is 1 less card in the deckafter we have called the _deal function.

    def test_deal_hand(self):
        """deal_hand should deal the amount of cards you define, and take them out of the deck of cards"""
        cards = self.deck.deal_hand(10) # we just have to use the same code as the test_deal_sufficent_cards test.
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_shuffle_low_cards(self):
        """shuffle should bring an error message up if there isnt a full deck to shuffle"""
        self.deck.deal_card() # deal 1 card out of the deck
        with self.assertRaises(ValueError): # check to see if the ValueError will be triggered (because there isnt a full deck of cards anymore)
            self.deck.shuffle() # try and shuffle and it will error. 

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the cards in the deck."""
        cards = self.deck.cards[:] # make a fresh deck of cards
        self.deck.shuffle() # shuffle the deck of cards
        self.assertNotEqual(cards, self.deck.cards) # check to see if the cards deck is not the same as the shuffled deck!
        self.assertEqual(self.deck.count(), 52) # also make sure the deck of cards is 52!

if __name__ == "__main__":
    unittest.main()

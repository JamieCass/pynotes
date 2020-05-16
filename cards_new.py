from random import shuffle

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:

    def __init__(self):
        #remember we need to have all 52 cards, so we need to do that now.
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Spades','Clubs','Hearts','Diamonds']
        self.cards = [Card(value,suit) for value in values for suit in suits]

    def __repr__(self):
        #we want to print out how many cards we have.
        return f'Deck of {self.count()} cards'

    def count(self):
        #we want just the number of cards so we can use it for shuffle and deal.
        return len(self.cards)

    def _deal(self, num):
        #we want to know the count of cards and make sure theres enough to deal with.
        count = self.count()
        #see what one is more out of count and the number of cards we want to deal.
        actual = min([count,num])
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,num):
        return self._deal(num)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full deck can be shuffled')
        shuffle(self.cards)
        return self

d = Deck()

d.count()

d
d._deal(1)
d.count()
d.deal_card()
d.deal_hand(2)
d.count()
d.shuffle()
d.cards
d

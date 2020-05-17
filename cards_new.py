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
        #here we are defining what self cards is. and thats every value in ever suit VERY IMPORTANT
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
        #now you define what cards is, which is what youre going to return
        cards = self.cards[-actual:]
        #you need to make sure the self.cards is updated by taking away whatever cards you just dealt.
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,num):
        return self._deal(num)
        #remember to return self._deal otherwise it wont show you the cards.
    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full deck can be shuffled')
        shuffle(self.cards)
        return self

#assign Deck as d
d = Deck()

#see how many cards in the deck
d.count()

d
#deal 1 card from the 'secret' function
d._deal(1)
#see if theres 1 less card in the deck
d.count()
#deal 1 card from the deal_card fuunction
d.deal_card()
#deal a hand of 2 cards
d.deal_hand(2)
#make sure there is the right amount of cards after all the dealing weve done
d.count()
#see if the shuffle works (it shouldnt because theres not a full deck)
d.shuffle()

d.cards
d

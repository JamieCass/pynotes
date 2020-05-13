from random import shuffle


# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'




# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.


class Deck:

    def __init__(self):
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(value,suit) for suit in suits for value in values]

        #for loop version

        # for suit in suits:
        #     for value in values:
        #         self.cars.append(Card(value,suit))
        # print(self.cards)

    #Will print how many are in the deck. calls it using the self.count().
    def __repr__(self):
        return f'Deck of {self.count()} cards'

    #Count how many cards are in the deck
    def count(self):
        return len(self.cards)

    #REMEMBER we dont usually call this. its just a function for the deal_card and deal_hand
    #To let us know if all cards have been dealt and define what deal is 'Allowed' to do and sort out the rest of the deck after cards are dealt.
    def _deal(self, num):
        count = self.count()
        #need to compare what one is lower out of count and whats left in the deck
        #min of count and number and compares what one is lower, if count is lower you will only be able to have however many cards are left.
        actual = min([count,num])
        #if theres no cards left we need an error to come up.
        if count == 0:
            raise ValueError('All cards have been dealt')
        #use slicing to take the actual amount of cards out of the deck
        cards = self.cards[-actual:]
        #then we need to redefine self.cards buy slicing again.
        self.cards = self.cards[:-actual]
        return cards

    #just want to deal one card.
    def deal_card(self):
        #self.deal(1) 1 card and we need to take it out of a 1 card list so we need to define [0] to actaully have the card.
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        #deal the number of cards you want to have in your hand.
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')

        #we are calling this shuffle from the random that we imported up the top. not the function.
        shuffle(self.cards)
        #just good practice, dont have to return self.
        return self

d= Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(3) 
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()
print(hand

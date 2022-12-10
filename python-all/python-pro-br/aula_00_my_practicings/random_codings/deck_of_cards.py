'''
References:
        - https://www.youtube.com/watch?v=t8YkjDH86Y4
        - https://github.com/eli-byers/Deck-Of-Cards-Python/blob/master/deckofcards.py

        Note: The code is as in the video-tutorial only but may be refactored
              to the github repo version! Have fun!
'''  

import random


class Card(object): # there's no difference between (object):, (): ou simply :
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()

    def show(self):
        print(f'{self.value} of {self.suit}')


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1, 14):
                self.cards.append(Card(s, v))  #print(f'{v} of {s}')

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()



# card = Card('Clubs', 6)
# card.show()

deck = Deck()
#deck.show()
deck.shuffle()
#deck.build()
deck.show()

# bob = Player('Bob')
# bob.draw(deck).draw(deck)
# bob.showHand()

# card = deck.drawCard()
# card.show()
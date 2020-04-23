import collections
from random import choice

#namedtuple = factory function for creating tuple subclasses with named fields
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')

print("define a card")
print(beer_card)

print("\ndefine a french deck and give the length")
deck = FrenchDeck()
print(len(deck))

print("\nget the first entry and the last")
print(deck[0])
print(deck[-1])

print("\nchoice gets a random item from a sequence")
print(choice(deck))

print("\nshow that the new class support slicing because we implement"+
" __getitem__")

print("top 3 from deck : ", deck[:3])
print("go to the 12th card and jump by 13 ", deck[12::13])

print("Because of __getitem__ deck is also iterable")
for card in deck:
    print(card)

print("Because of __getitem__ deck is also iterable in reverse")
for card in reversed(deck):
    print(card)


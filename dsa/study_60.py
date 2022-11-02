# python 中 set、dict均是基于hash表，==,eq

from collections import namedtuple
Card = namedtuple('Card',['rank','suit'])

class FranchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['红心', '方片', '梅花', '黑桃']

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in FranchDeck.ranks for suit in FranchDeck.suits]

    def __len__(self):
        return self._cards.__len__()

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

deck = FranchDeck()
print(deck[3])
print(deck.__len__())
from random import choice,shuffle
shuffle(deck)#会改变每个索引对应的值，所以需要__setitem__
print(deck[3])
print(deck[:3])
print(choice(deck))

print(choice(deck))



# pickle
# shelve
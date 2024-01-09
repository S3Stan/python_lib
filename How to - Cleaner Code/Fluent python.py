import collections

card = collections.namedtuple('Card', ['rank' 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [card(rank, suit) 
                       for suit in self.suits
                       for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    
    
demo_card = card('5', 'hearts')
demo_card

             
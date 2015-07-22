"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


     
    def has_pair(self):
        lis=self.cards[:]
        for card1 in self.cards:
              lis.remove(card1)
              for card2 in lis:
                  if card1.rank==card2.rank:
                     return True
                  
        return False


   
    def has_two_pair(self):
        c=0
        l=self.cards[:]
        for card1 in self.cards:
            l.remove(card1)
            for card2 in l:
               if card1.rank==card2.rank:
                    c=c+1
        if c==2:
           return True
        else:
            return False
    
    def three_of_kind(self):
        lis=self.cards[:]
        for card1 in self.cards:
            lis.remove(card1)   
            li=lis[:]
            for card2 in lis:
                li.remove(card2)
                for card3 in li:
                      if card1==card2==card3:
                            return True
        return False


 

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print "has flush",'    ',hand.has_flush()
        print "has pair","      ",hand.has_pair()
        print "has two pair","     ",hand.has_two_pair()
        print "has 3 of kind","     ",hand.three_of_kind()
        print ''

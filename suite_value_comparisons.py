""" Module for assessing if two cards are the same number or suite

The functions of this module use card index numbers 1-52 and creates the lists
for values that are same for each type of suite and card value and
then compare if the inputted card index values belong to the same list and
return True or False.

Public methods:
- cardnum_comparison: compare if two cards have the same value based on their
index number
- suites_comparison: compare if two cards are the same suite based on their
index
"""


class Suite_value_comparison(object):
   
    def __init__(self):
        
        # Create a list of cards in each suit
        self._suites_twodim_list = [[(x+1)+(y*13) for x in range(13)]
                                    for y in range(4)]
        
        # Create a list of cards in each value
        self._cardnum_twodim_list = [[(x*13)+(y+1) for x in range(4)]
                                     for y in range(13)]

    def cardnum_comparison(self, xx, yy):
        """ Compares if two cards have the same number value in card number 
        terms.
        
        Args: index values of any two cards from a deck indexed from 1 to 52
        
        Returs: True if same number, False if not
        """
        
        # Run a test of same numberdness across suites
        for y in range(4):
            for x in range(4):
                try:
                    if (self._suites_twodim_list[y].index(xx) ==
                            self._suites_twodim_list[x].index(yy)):
                        return True
                    else:
                        return False
                except(ValueError):
                    pass

    def suites_comparison(self, xx, yy):
        """ Compares if two cards are the same suite.
        
        Args: index values of any two cards from a deck indexed from 1 to 52
        
        Returs: True if same suite, False if not
        """
        
        # Run a test of same suiteness across numbers
        for y in range(13):
            for x in range(13):
                try:
                    if (self._cardnum_twodim_list[y].index(xx) ==
                            self._cardnum_twodim_list[x].index(yy)):
                        return True
                    else:
                        return False
                except(ValueError):
                    pass

    def value_comparison(self, xx, yy):
        return self.suites_comparison(xx, yy) or self.cardnum_comparison(xx, yy)


if __name__ == '__main__':
    """Tests and demonstrates the use of the module
    
    Shufles a 52 card deck and compares the two top cards at the time to each
    other until the whole deck is gone through.
    """

    import random
    import deck_convert
    
    converted = deck_convert.Deck_convert()
    test_use = Suite_value_comparison()
    
    deck = list(range(1, 53))
    random.shuffle(deck)
    for x in range(25):
        card1 = deck.pop(0)
        card2 = deck.pop(0)
        dkc1 = converted.deck_key_convert(card1)
        dkc2 = converted.deck_key_convert(card2)
        print(card1, card2, dkc1, dkc2)
        print('\t', "same number: ", test_use.cardnum_comparison(card1, card2))
        print('\t', "same suite: ", test_use.suites_comparison(card1, card2))
        print('\t', "same number or suite: ", test_use.value_comparison(card1,
        card2))
        
        
    

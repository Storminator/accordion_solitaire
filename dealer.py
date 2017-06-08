import random
import deck_convert

"""Creates and shuffles a deck, deals cards and prints the cards on table
"""

converted = deck_convert.Deck_convert()

class Dealer(object):
    
    def __init__(self):
        """Initializes a 52 card deck, shufles it and creates a table to deal
        on """
        self.dealer_deck = list(range(1, 53))
        random.shuffle(self.dealer_deck)
        self.table_deck = []
         
    def deal_cards(self, x):
        """Deals x number of cards to the table"""
        for y in range(x):
            self.table_deck.append(self.dealer_deck[0])
            del self.dealer_deck[0]

    def cards_on_table(self):
        """Show the cards on the table
        
        This function prints the position of all the cards on the table and
        converts the value to card symbols by using the deck_convert module"""
        
        print('Card place index')
        for x in self.table_deck:
            y = str(self.table_deck.index(x) + 1)
            print(y, (3 - len(y))*' ', end='')
        print('')
        print('Card numbers')
        for x in self.table_deck:
            y = converted.deck_key_convert(x)
            print(y,(3-len(y))*' ',end='')
        print('')

    def deal_and_show(self, x):
        """Combines two differend methods to both deal new cards and show them"""
        self.deal_cards(x)
        self.cards_on_table()

    def move_and_replace(self, xx, x):
        """ Moves a chosen card from the table and replaces another one with it

        Args: 
        xx is the index number of the card you want do the replacement with 
        x is the distance from your replacing card you want to replace towards
        the beginning of the table"""
        
        y = xx - 1
        z = self.table_deck[y]
        del self.table_deck[y]
        del self.table_deck[y - x]
        self.table_deck.insert(y - x, z)
 
    
if __name__ == '__main__':
    """This is a simple test for all the functions in the module dealer"""

    test_deal = Dealer()
    test_deal.deal_cards(2)
    test_deal.cards_on_table()
    print('-----')
    test_deal.deal_and_show(1)
    print('-----')
    test_deal.move_and_replace(3, 1)
    test_deal.cards_on_table()

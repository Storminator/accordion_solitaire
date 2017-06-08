"""This module converts card index numbers(1-52) to card symbol and value pairs

The module creates a list of unicode based card symbols, and then uses that
list to convert the game situation to card symbols for the user

Available class:
- Deck_convert: convert index number to unicode based card symbol
"""


class Deck_convert(object):
    """This class converts card index numbers to card symbols
    """
    
    def __init__(self):
        
        # Create lists containing value card symbols and
        # unicode characters u2660-3 of suites
        value_card_list = ['J', 'Q', 'K', 'A']
        unicode_symbol_list = ['\u2660', '\u2661', '\u2662', '\u2663']

        # Create an empty list to hold all card values
        self._deck_values = []

        # Combine numbers, unicode suite symbols and value card symbols
        for unicode in unicode_symbol_list:
            for suit in range(2, 11):
                z = unicode + str(suit)
                self._deck_values.append(z)
            for symbol in value_card_list:
                z = unicode + symbol
                self._deck_values.append(z)
                
    def deck_key_convert(self, card):
        """Convert card index number to unicode card symbol
        
        Args: card index number
        Returns: card symbol"""
        
        self._deck_key_convert = self._deck_values[card-1]
        
        return self._deck_key_convert

          
if __name__ == '__main__':
    """The card value number conversion is tested
    with a full shufled deck"""
    
    import random
    
    use = Deck_convert()
    
    # Create a shufled deck
    x = list(range(1, 53))
    random.shuffle(x)
    
    # Print the index numbers of the deck
    for z in x:
            print(z, (3-len(str(z)))*' ', end='')
    print('')
    
    # Convert and print each card value
    for y in x:
        r = use.deck_key_convert(y)
        print(r, (3-len(str(r)))*' ', end='')

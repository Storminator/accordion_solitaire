#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

"""This is the main module for playing accordion solitaire in command line.

This module allows you to play accordion solitaire without GUI in your command
line.

important function:
    accordion_game_loop: implements game logic in a loop
"""

# TO-DO: save the last input to a list for undo
# TO-DO: create an event module for handling user input

import random
import dealer
import suite_value_comparisons


# Create an instance of Suite_value_comparison class
svc = suite_value_comparisons.Suite_value_comparison()

# Create and instance of the Dealer class
deck = dealer.Dealer()

def accordion_game_loop():
    """ This is the main game loop for playing accordion solitaire"""

    while True:
            
        # Shows player the cards on the table
        deck.cards_on_table() 
   
        # Prompt player to choose from available cards on table or quit
        player_choice = input(
            "Pick a card index number or deal a card = d or quit game = q: ")
        print('')
    
        try:
            # How to exit the game loop
            if player_choice == 'q':
                break
            # How to deal a new card, plus win and lose conditions 
            if player_choice == 'd':
                if len(deck.dealer_deck) >= 1:
                   deck.deal_cards(1)
                   print('Undealt cards: ', len(deck.dealer_deck), '\n')
                   continue
                if len(deck.dealer_deck) == 0 and len(deck.table_deck) == 1:
                    print('\n','\t','Congratulations, you won!')
                    break
                else:
                    break
                
            # How to choose a particular card and move it 3 or 1 places
            if 1 <= int(player_choice) <= 53:
                player_choice1 = int(player_choice)
                player_choice2 = input(
                    "please choose d = deal, 3 = move 3 places or 1 = move one place: ")
                
                # Repeating the dealing of a new card plus win and loose
                # conditions
                if player_choice2 == 'd':
                    if len(deck.dealer_deck) >= 1:
                       deck.deal_cards(1)
                       print('Undealt cards: ', len(deck.dealer_deck), '\n')
                       continue
                    if len(deck.dealer_deck) == 0 and len(deck.table_deck) == 1:
                        print('\n','\t','Congratulations, you won!')
                        break
                    else:
                        break
                    
                # How to move card 3 places and check that it is possible
                elif (player_choice2 == '3' and 
                      svc.value_comparison(
                      deck.table_deck[player_choice1 - 1],
                      deck.table_deck[player_choice1 - 4])):
                    if len(deck.table_deck) >= 4:
                        deck.move_and_replace(player_choice1, 3)
                    elif len(deck.dealer_deck) == 0 and len(deck.table_deck) == 1:
                        print('\n','\t','Congratulations, you won!')
                    else:
                        print('\n','\t','*** Please choose again, move not allowed ***','\n')
                        continue

                # How to move card 1 places and check that it is possible
                elif (player_choice2 == '1' and 
                      svc.value_comparison(
                      deck.table_deck[player_choice1 - 1],
                      deck.table_deck[player_choice1 - 2])):
                    if len(deck.table_deck) > 1:
                        # Choosing to add to next
                        deck.move_and_replace(player_choice1, 1)
                    elif len(deck.dealer_deck) == 0 and len(deck.table_deck) == 1:
                        print('\n','\t','Congratulations, you won!')
                    else:
                        print('\n','\t','*** Please choose again, move not allowed ***','\n')
                else:
                    print('\n','\t','*** Please choose again, move not allowed ***','\n')
                            
        # Indicate that the player has chosen unknown command
        except:
            print(3 * '\n','\t','!!! Unknown command, please choose again !!!','\n')
            continue
    
    print('Thanks for playing!')

start = input('Want to play accordion y/n?: ')
try:
    if start == 'y':
        deck.deal_cards(2)
        accordion_game_loop()
except:
    None



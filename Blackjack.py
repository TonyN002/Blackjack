import random

# Initialize global constants.
CLUBS = chr(9827)       # Character 9827 is '♣'.
DIAMONDS = chr(9830)    # Character 9830 is '♦'.
HEARTS = chr(9829)      # Character 9829 is '♥'.
SPADES = chr(9824)      # Character 9824 is '♠'.

BACKSIDE = 'backside'   # Used to print back of dealer's card.

def display_cards(cards):
    """
    Display all the cards in the cards list.
    The parameter cards will represent a player
    or dealer's hand.

    This function is called by the display_hands() function.

    Parameters:
        cards (list): the list of cards to display

    Example:
        See See Section 2.4.4.2, Test #1 for an example.
        Each of row of cards - one row for the Dealer and
        one row for the Player - are shown using
        this display_cards() function.
    """

    # The text to display on each row.
    rows = ['', '', '', '', '', '', '']

    for card in cards:
        # Print the top line of the card.
        rows[0] += ' ________   '

        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '| ##     |  '
            rows[2] += '|        |  '
            rows[3] += '|  ###   |  '
            rows[4] += '|        |  '
            rows[5] += '|    ##  |  '
            rows[6] += '|________|  '
        else:
            # Print the card's front.
            # The card is a list data structure of length 2
            # that consists of a rank and a suit.
            rank, suit = card
            rows[1] += '| {}     |  '.format(rank.ljust(2))
            rows[2] += '|        |  '
            rows[3] += '|   {}   |  '.format(suit.ljust(2))
            rows[4] += '|        |  '
            rows[5] += '|     {} |  '.format(rank.rjust(2))
            rows[6] += '|________|  '

    # Print each row of the cards on the screen:
    for row in rows:
        print(row)

def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """
    Show the player's and dealer's cards. Hide the dealer's first
    card if show_dealer_hand is False. Otherwise, show the dealer's
    first card if show_dealer_hand is True.

    Parameters:
        player_hand (list): the list of cards in the player's hand.
        dealer_hand (list): the list of cards in the dealer's hand.
        show_dealer_hand (bool): boolean denoting whether to show the
                                   dealer's first card face-up.

    Examples:
       See Section 2.4.4.2, Test #1 for an example
         that shows the dealer's first card face-up.
    """

    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards:
    print()
    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)
    print('\n')
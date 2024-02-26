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

def draw_card(deck):
    """
    Returns and removes the top (first) card from the deck.
    After the draw_card function, the deck contains one less card.

    Parameters:
        deck (list): the deck of cards to draw from

    Returns:
        card (list): rank and suit of card drawn

    Examples:
        >>> draw_card(get_shuffled_deck())
        ('Q', '♣')

        >>> draw_card(get_shuffled_deck())
        ('2', '♥')
    """
    return deck.pop()

def get_move():
    """
    Asks the player for their move, and returns 'h' for hit
    or 's' for stand.

    Returns:
        move (str): 'h' for hit or 's' for stand

    Examples:
        >>> get_move()
        's'

        >>> get_move()
        'h'
    """

    # Loop until the player enters a valid move.
    is_valid_move = False
    while not is_valid_move:
        user_input = input('[h]it or [s]tand  > ')
        move = user_input.lower()
        if move in ['h', 's', 'hit', 'stand']:
            is_valid_move = True
    return move

def get_shuffled_deck():
    """
    Return a shuffled deck of 52 cards.

    Each playing card can be represented using two characters. The
    first character is the value of the card, with the values 2
    through 10 being represented directly. The characters 'J', 'Q',
    'K' and 'A' are used to represent the values Jack, Queen,
    King and Ace, respectively.

    The second character is a character code that represents the
    suit of the card: '♠' for spades, '♥' for hearts, '♦' for diamonds
    and '♣' for clubs.

    Returns:
        list: representing the deck of 52 cards, where each card is
                a list of tuples of rank and suit

    Example:

        >>> get_shuffled_deck()
        [('K','♣'), ('10', '♥'), ('A', '♣'), ('9', '♦'), ('2', '♠'), ...]
    """

    # Initialize cards in the deck.
    deck = []
    for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8',
                     '9', '10', 'J', 'Q', 'K']:
            deck.append((rank, suit))

    # Shuffle the cards in the deck.
    random.shuffle(deck)

    return deck

def is_playing_again():
    """
    Returns whether the user wants to play again.

    Returns:
        bool: True if user wants to play again. False otherwise.
    """

    is_valid_response = False
    while not is_valid_response:
        play_again = input("Play again? [y]es or [n]o  > ")
        if play_again.lower() in ['y', 'n', 'yes', 'no']:
            is_valid_response = True

    if play_again.lower() == 'y':
        return True
    return False

def press_enter_to_continue():
    """
    Pauses the screen until the enter key is pressed.
    """

    input('Press Enter to continue...')
    print('\n\n')

def print_welcome_message():
    """
    Prints welcome message for Blackjack game.
    """

    print()
    print('Welcome to Blackjack!')
    print()
    print('Rules:')
    print('- Get as close to 21 without going over.')
    print('- Kings, Queens, and Jacks are worth 10 points.')
    print('- Aces are worth 1 or 11 points.')
    print('- Cards 2 through 10 are worth their face value.')
    print()
    print('- For gameplay, press h or s.')
    print('  [h]it to take another card.')
    print('  [s]tand to stop taking cards.')
    print()

def play_blackjack():
    """
    The main driver for the Blackjack game.
    """

    # Provide a welcome screen.
    print_welcome_message()

    # Begin gameplay.
    is_playing_blackjack = True

    while is_playing_blackjack:
        # Reset that player does not have Blackjack.
        has_blackjack = False

        # Create new shuffled deck.
        deck = get_shuffled_deck()

        # Give the dealer and player two cards from the deck.
        dealer_hand = [draw_card(deck), draw_card(deck)]
        player_hand = [draw_card(deck), draw_card(deck)]

        # Show the initial hands. The dealer's first card is hidden.
        display_hands(player_hand, dealer_hand, False)

        # Handle player and dealer actions.
        if get_hand_value(player_hand) < 21:
            get_player_moves(deck, player_hand, dealer_hand)

            # Get dealer moves. Make sure player has not bust.
            if get_hand_value(player_hand) <= 21:
                get_dealer_moves(deck, player_hand, dealer_hand)
        display_hands(player_hand, dealer_hand, True)

        # Display if player won or lost.
        game_result = get_game_outcome(player_hand, dealer_hand)
        print(game_result)

        # Continue playing or exit the game.
        is_playing_blackjack = is_playing_again()

def get_hand_value(cards):
    """
    Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value).

    Parameters:
        cards (list): the list of cards to score. Each card in
                        the list is also a list composed of a
                        rank and suit.

    Returns:
        int: the total value of the cards

    Examples:
        >>> get_hand_value([('2', CLUBS), ('4', DIAMONDS), ('K', DIAMONDS),
                            ('3', SPADES)])
        19

        >>> get_hand_value([('10', SPADES), ('A', HEARTS)])
        21
    """
#Separate rank from suits for hand seeing that suits aren't needed to calculate value
    hand_rank = [rank[0] for rank in cards]
    sum_rank = 0

#assigns values to no-Ace ranks and sums
    for rank in hand_rank:
      if rank in "JQK":
        sum_rank += 10
      elif rank.isdigit():
        sum_rank += int(rank)

#if Ace assign 1 or 11 based on total hand value
    for rank in hand_rank:
      if rank in "A" and (sum_rank + 11 <= 21):
        sum_rank += 11
      elif rank in "A" and (sum_rank + 11 > 21):
        sum_rank += 1

    return sum_rank
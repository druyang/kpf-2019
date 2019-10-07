#
# A Single Player Blackjack Card Game
# Code for Kleiner Perkins Engineering Challenge
# Written by Andrw Yang
#

from card_framework import*

def game():
    global first_game
    """Method to play/run the game"""
    playing = True
    while playing:
        game_over = False
        deck = Deck()
        deck.shuffle()

        if first_game:
            player = Player()
            dealer = Player(True)
            first_game = False

        player.new_hand()
        dealer.new_hand()

        for i in range(2):
            player.hand.add_card(deck.deal())
            dealer.hand.add_card(deck.deal())

        print("-----")
        print("Welcome to Blackjack! Your bank is: " + str(player.bank))
        player.bet = input("How much would you like to bet? ")
        while not player.bet.isdigit() or int(player.bet) > player.bank:
            player.bet = input("Please enter a digit like '10' or '300' under or equal to your bank value")

        print("-----")
        print("Dealers hand is:")
        dealer.hand.display()
        print("Player 1's Hand is:")
        player.hand.display()

        while not game_over:
            player_has_blackjack, dealer_has_blackjack = player.check_for_blackjack(), dealer.check_for_blackjack()

            if player_has_blackjack or dealer_has_blackjack:
                game_over = True
                if player_has_blackjack:
                    player.bank += int(player.bet) * 3 / 2
                    game_over = True
                elif dealer_has_blackjack:
                    player.bank -= int(player.bet)
                    game_over = True
                continue

            # Need to implement Double, Split, and Surrender. Split may be hard
            choice = input("Please choose [Hit / Stick] ").lower()
            while choice not in ["h", "s", "hit", "stick"]:
                choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()

            # If the player hits, it adds a card
            if choice in ['hit', 'h']:
                player.hand.add_card(deck.deal())
                player.hand.display()
                if player.is_over():
                    print("You have lost!")
                    player.bank -= int(player.bet)
                    game_over = True
            else:
                # Dealer hits if value less than 17
                while dealer.hand.value < 17:
                    dealer.hand.add_card(deck.deal())
                    dealer.hand.calculate_value()
                    if dealer.check_for_blackjack():
                        print("You have lost!")
                        player.bank -= int(player.bet)
                        game_over = True
                player_hand_value = player.hand.calculate_value()
                dealer_hand_value = dealer.hand.calculate_value()

                print("-----")
                print("Final Results")
                print("Your hand:")
                player.hand.display()
                print("Dealer's hand:")
                dealer.hand.display()

                # Check for black jack and compare scores, handle bet and bank
                if player_hand_value > dealer_hand_value or dealer_hand_value > 21:
                    player.bank += int(player.bet)
                    print("You win!")
                    if player_has_blackjack:
                        player.bank += int(player.bet) * 3 / 2
                elif player_hand_value == dealer_hand_value:
                    print("It's a tie!")
                elif player_hand_value < dealer_hand_value:
                    player.hand -= int(player.bet)
                    print("Dealer wins!")
                game_over = True

        runItBack = input("Play Again? [Y/N] ")
        while runItBack.lower() not in ["y", "n", "yes", "no"]:
            runItBack = input("Please enter Y or N ")
        if runItBack.lower() == "n":
            print("Thanks for playing!")
            playing = False
        else:
            game_over = False

if __name__ == '__main__':
    first_game = True
    game()
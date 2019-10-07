from random import*
class Card:
    """Class for each card"""
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        s = self.num + " of " + self.suit
        return s

class Deck:
    """Class for a deck of 52 cards (no jokers)"""
    def __init__(self):
        # Creates a deck of cards in a list
        self.deck = [Card(n, s)
                     for n in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
                     for s in ["Clubs", "Spades", "Diamonds", "Hearts"]]

    def shuffle(self):
        """Shuffles the Deck using random"""
        if self.deck:
            shuffle(self.deck)

    def deal(self):
        """Deals a card by returning and removing the top card"""
        if self.deck:
            return self.deck.pop()

class Hand:
    """Class for card handling for a Blackjack hand"""
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        """Adds a card to a hand"""
        self.cards.append(card)

    def calculate_value(self):
        """Calculates the value of a hand with ace being 1 or 11 and face cards being 10"""
        self.value = 0
        ace = False
        for card in self.cards:
            if card.num.isnumeric():
                self.value += int(card.num)
            elif card == "A":
                self.value += 11
                ace = True
            else:
                self.value += 10

        # Correct for going over 21 if there is an ace
        if self.value > 21 and ace == True:
            self.value -= 10
        return self.value

    def display(self):
        for card in self.cards:
            print(card)

class Player:
    """Class for each player"""
    def __init__(self, isDealer = False):
        self.bank = 1000
        self.bet = 0
        self.hand = Hand()
        self.blackjack = False
        self.isOver = False
        self.isDealer = isDealer

    def is_over(self):
        """Returns if the player has busted, must have called calculate_value before this"""
        self.hand.calculate_value()
        if self.hand.value > 21:
            self.isOver = True
        return self.isOver

    def check_for_blackjack(self):
        """Checks for blackjack, must have called calculate_value before this"""
        return self.hand.value == 21

    def calculate_results(self):
        if self.check_for_blackjack():
            if self.isDealer == False:
                self.bank *= 1.5
            return True

    def new_hand(self):
        self.hand = Hand()


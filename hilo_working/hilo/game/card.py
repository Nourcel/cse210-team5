
# Card Class
# CSE210 By Robert Odell

import random

class Card:
    """
     Class represents one card

     ...

     Attributes
     -----------

     __value = (between 1-13)
     
     __suit = (between 1-4)

     Methods
     ---------

     Shuffle = Randomly change value and suit of card
     
     get_suit = return suit
     
     get_suit_string = returns the card suit as a string
     
     set_suit = set suit to new #
     
     get_value = return value
     
     get_value_string = returns the card value as a string
     
     set_value = set value to new #
     
     card_name = returns the card name as a string ex:'King of Clubs'

     Properties
     ----------

     value = card value (1-13)

     suit = card suit (1-4)

    """

    # Constant variable - suits
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

    # Constant variable - values
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __init__(self):
        self.__value = 1
        self.__suit = self.CLUB
        self.shuffle()

    # Set value to random number

    def shuffle(self):
        self.__value = random.randint(1, 13)
        self.__suit = random.randint(1, 4)

    # Returns card suit

    def get_suit(self):
        return self.__suit

    # Returns the card suit as a string

    def get_suit_string(self):
        if self.suit == 1:
            return "Club"
        elif self.suit == 2:
            return "Diamond"
        elif self.suit == 3:
            return "Heart"
        elif self.suit == 4:
            return "Spade"

    # Sets card suit

    def set_suit(self, value):
        self.__suit = value

    # Returns card value

    def get_value(self):
        return self.__value

    def get_value_string(self):

        if self.value == 1:
            return "Ace"
        elif self.value == 2:
            return "Two"
        elif self.value == 3:
            return "Three"
        elif self.value == 4:
            return "Four"
        elif self.value == 5:
            return "Five"
        elif self.value == 6:
            return "Six"
        elif self.value == 7:
            return "Seven"
        elif self.value == 8:
            return "Eight"
        elif self.value == 9:
            return "Nine"
        elif self.value == 10:
            return "Ten"
        elif self.value == 11:
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13:
            return "King"

    # Sets card value

    def set_value(self, value):
        self.__value = value

    # Returns the string expression of a card
    # Example: 'King of Clubs'

    def card_name(self):
        return (f"{self.get_value_string()} of {self.get_suit_string()}s")

    suit = property(get_suit, set_suit)

    value = property(get_value, set_value)




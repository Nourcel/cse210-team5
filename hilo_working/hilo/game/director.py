from game.card import Card

"""
Cameron Barrett
Director Class in progress
CSE 210
"""

class Director:
    def __init__(self):
        self.first_card = {}
        self.next_card = {}
        self.is_playing = True
        self.points = 0
        self.total_score = 300

        # card1 = Card()
        # card2 = Card()
        # self.first_card.append(card1)
        # self.next_card.append(card2)

    def start_game(self):
        while self.is_playing:
            # self.first_deal()
            self.do_updates()
            self.play_again()

    # def first_deal(self):
    #     # card1 = ""
    #     # for i in range(len(self.first_card)):
    #     #     card = self.first_card[i]
    #     #     card1 = card.card_name()
    #     """
    #     for i in range(1):
    #         card = Card()
    #         card1 = card.card_name()
    #         self.first_card.append(card1)
    #     """
    #     card1 = Card()
    #     card_dict = {card1.card_name(): card1.get_value()}
    #     self.first_card.update(card_dict)

    #     for key, value in self.first_card.items():
    #         card_key1 = key
    #         card_value1 = value
    #     print(f"\nThe card is: {card_key1}")

    #     self.draw_card = ""
    #     self.draw_card = input("Higher or lower? [h/l] ").lower()
    #     while self.draw_card != "h" and self.draw_card != "l":
    #         print("\nPlease Type h of Higher or l for Lower")
    #         self.draw_card = input("Higher or lower? [h/l] ").lower()

    def do_updates(self):
        if not self.is_playing:
            return
        # card2 = ""
        # for i in range(len(self.next_card)):
        #     card = self.next_card[i]
        #     card2 = card.card_name()
        """
        for i in range(1):
            card = Card()
            card2 = card.card_name()
            self.next_card.append(card2)
        """
        card1 = Card()
        card_dict = {card1.card_name(): card1.get_value()}
        self.first_card.update(card_dict)

        for key, value in self.first_card.items():
            card_key1 = key
            card_value1 = value
        print(f"\nThe card is: {card_key1}")

        self.draw_card = ""
        self.draw_card = input("Higher or lower? [h/l] ").lower()
        while self.draw_card != "h" and self.draw_card != "l":
            print("\nPlease Type h of Higher or l for Lower")
            self.draw_card = input("Higher or lower? [h/l] ").lower()

        card2 = Card()
        card_dict = {card2.card_name(): card2.get_value()}
        self.next_card.update(card_dict)
        
        # for i in range(len(self.next_card)):
        #     dealt_card = self.next_card[i]
        # print(f"Next card was: {dealt_card}")
        for key, value in self.next_card.items():
            card_key2 = key
            card_value2 = value
        print(f"Next card was: {card_key2}")
            # print(value)
        # card1 = self.first_card
        # card2 = self.next_card

        if card_value1 < card_value2 and self.draw_card == "h":
            self.points = 100
        elif card_value1 > card_value2 and self.draw_card == "l":
            self.points = 100
        elif card_value1 > card_value2 and self.draw_card == "h":
            self.points = -75
        elif card_value1 < card_value2 and self.draw_card == "l":
            self.points = -75
        else:
            self.points = 0
        self.total_score += self.points

        print(f"Your score is: {self.total_score}")
        

    def play_again(self):
        if self.is_playing == (self.total_score > 0):
            deal = ""
            deal = input("Play again? [y/n] ").lower()
            while deal != "y" and deal != "n":
                print("\nPlease type y for Yes or N for No.")
                deal = input("Play again? [y/n] ").lower()
            self.is_playing = (deal == "y")
            if deal == "n":
                print(f"Your score is: {self.total_score}\nThanks for playing!")
        else:
            self.is_playing = print("Game Over")
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

    def start_game(self):
        while self.is_playing:
            self.deal()
            self.play_again()

    def deal(self):
        if not self.is_playing:
            return

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

        self.card2 = Card()
        self.card_dict = {self.card2.card_name(): self.card2.get_value()}
        self.next_card.update(self.card_dict)

        for key, value in self.next_card.items():
            card_key2 = key
            card_value2 = value
        print(f"Next card was: {card_key2}")

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
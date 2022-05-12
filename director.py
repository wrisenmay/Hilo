from card import Card

class Director:

    def __init__(self):
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        while self.is_playing == True:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        card = Card()
        self.cards = card.draw()
        print(f"The first card is: {self.cards[0]}")
        self.hilo = input("Higher or lower? [h/l] ").lower()
        print(f"The next card is: {self.cards[1]}")
    
    def do_updates(self):
        if self.is_playing == False:
            return
        if self.hilo == ("h") and self.cards[0] < self.cards[1] or self.hilo == ("l") and self.cards[0] > self.cards[1]:
            self.score = 100
        else:
            self.score = -75
        self.total_score += self.score

    def do_outputs(self):
        if self.is_playing == False:
            return
        print(f"Your score is: {self.total_score}")
        if self.total_score <= 0:
            self.is_playing = False
            print("You've lost all of your points. Game over.")
        self.play = input(f"Play again? [y/n] ").lower()
        if self.play == "y":
            print()
            self.is_playing = True
        else:
            print("Thanks for playing!\n")
            self.is_playing = False
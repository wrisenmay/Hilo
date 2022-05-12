import random

class Card:
    def __init__(self):
        self.cards = []
        self.card1 = 0
        self.card2 = 0

    def draw(self):
        self.card1 = random.randint(1,13)
        self.card2 = random.randint(1,13)
        self.cards.append(self.card1)
        self.cards.append(self.card2)
        return self.cards

 
import random

CLUBS = 1; DIAMONDS = 2; HEARTS = 3; SPADES = 4

SUITS = { 1: "Clubs", 2: "Diamonds", 3: "Hearts", 4: "Spades"}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        return

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return SUITS[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for rank in range(1,14):
            for suit in [CLUBS, DIAMONDS, HEARTS, SPADES]:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        return "Shuffle OK."

    def draw(self):
        return self.cards.pop()

    def get_size(self):
        return self.cards.len()

    def show(self):
        print("-~=  DECK  =~-")
        for card in self.cards:
            print(f"{card.rank} of {SUITS[card.suit]}")
        print("-~= \DECK  =~-")
        return "Print OK."

class Game():
    def __init__(self):
        print("New game started.") 

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
        return len(self.cards)

    def show(self):
        print("-~=  DECK  =~-")
        for card in self.cards:
            print(f"{card.rank} of {SUITS[card.suit]}")
        print("-~= \DECK  =~-")
        return "Print OK."

    def new_from_pile(self, pile):
        print("Making new deck from pile...")
        self.cards = pile.cards[-2::-1] # this is like flipping the pile over to make the new deck
        pile.cards = [pile.cards[-1]]
        return

class Game():
    def __init__(self):
        print("New game started.") 

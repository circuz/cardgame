# Testing different strategies for the card game 31

from cardgame_setup import Game, Deck, Card, SUITS
import game_31_knock_immediately
import game_31_knock_over_20
import game_31_knock_over_20_toss_best

class Player:
    def __init__(self, game, strategy = game_31_knock_immediately.strategy, points = 0):
        self.game = game
        self.points = points
        self.hand = []
        self.strategy = strategy

    def pull(self):
        self.hand.append(self.game.deck.draw())
        return
    
    def drop(self, card):
        self.hand.remove(card)
        self.game.pile.put(card)
        return

    def knock(self):
        self.game.knock(self)
        return

    def take_turn(self, pile):
        self.strategy(self, pile)
        return

    def give_point(self):
        self.points += 1
        return

    def show(self):
        print("-~= PLAYER =~-")
        for card in self.hand:
            print(f"{card.rank} of {SUITS[card.suit]}")
        print("-~=\PLAYER =~-")

    def tally(self):
        sums = [-1,0,0,0,0]
        for card in self.hand:
            if card.rank in range(2,10):
                sums[card.suit] += card.rank
            elif card.rank > 10:
                sums[card.suit] += 10
            else:
                sums[card.suit] += 11
        return sums

class Pile:
    def __init__(self, card = None):
        self.card = card
        return

    def put(self, card):
        self.card = card 
        return

    def get(self):
        return self.card

    def show(self):
        print("-~= PILE =~-")
        print(f"{self.card.rank} of {SUITS[self.card.suit]}")
        print("-~=\PILE =~-")
        return "OK"

class Game_31(Game):
    def __init__(self):
        print("New game started.") 
        self.knocked = False

        self.deck = Deck()
        self.deck.shuffle()
        #self.deck.show()

        player1 = Player(self, game_31_knock_over_20.strategy)
        player2 = Player(self, game_31_knock_over_20_toss_best.strategy)
        self.players = [player1, player2]

        for _ in range(3):
            player1.pull()
            player2.pull()
        player1.show()
        player2.show()

        self.pile = Pile()
        self.pile.put(self.deck.draw())
        self.pile.show()

        self.take_turns() # This will keep going until game ends
        return

    def show(self):
        print(f"PILE: {self.pile.card.rank} of {SUITS[self.pile.card.suit]}")
        print(f"Size of deck: {len(self.deck.cards)}")

    def take_turns(self):
        for player in self.players:
            if self.knocked != player:
                player.take_turn(self.pile)
            else:
                self.end_round()
                return
        self.show()
        self.take_turns()
        return

    def end_round(self):
        winner = None
        tally = 0
        for p, player in enumerate(self.players):
            if max(player.tally()) > tally:
                winner = p
                tally = max(player.tally())
        self.players[winner].give_point()
        
        print(f"Player {winner+1} wins with a score of {max(self.players[winner].tally())}!")
        return

    def knock(self, player):
        if not self.knocked:
            self.knocked = player
        return

def start_game():
    game = Game_31()
start_game()

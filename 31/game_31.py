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

    def pull(self, pile = False):
        if pile:
            self.hand.append(self.game.pile.get())
        else:
            self.hand.append(self.game.deck.draw())
        return
    
    def drop(self, card):
        self.hand.remove(card)
        self.game.pile.put(card)
        return

    def hand_size(self):
        return len(self.hand)

    def knock(self):
        self.game.knock(self)
        return

    def take_turn(self, pile):
        self.strategy(self, pile)
        return

    def give_point(self):
        self.points += 1
        return

    def get_points(self):
        return self.points

    def show(self):
        print("-~= PLAYER =~-")
        for card in self.hand:
            print(f"{card.rank} of {SUITS[card.suit]}")
        print("-~=\PLAYER =~-")

    def tally(self, extra_cards = []):
        sums = [-1,0,0,0,0]
        for card in self.hand + extra_cards:
            if card.rank in range(2,10):
                sums[card.suit] += card.rank
            elif card.rank > 10:
                sums[card.suit] += 10
            else:
                sums[card.suit] += 11
        return sums

class Pile:
    def __init__(self, cards = []):
        self.cards = cards
        return

    def put(self, card):
        self.cards.append(card)
        return

    def get(self):
        return self.cards.pop()

    def peek(self):
        return self.cards[-1]

    def show(self):
        print("-~= PILE =~-")
        print(f"{self.cards[-1].rank} of {SUITS[self.cards[-1].suit]}")
        print("-~=\PILE =~-")
        return "OK"

class Game_31(Game):
    def __init__(self):
        print("New game started.") 
        
        player1 = Player(self, game_31_knock_over_20.strategy)
        player2 = Player(self, game_31_knock_over_20.strategy)
        self.players = [player1, player2]
        
        self.setup()
        
        while self.players[1].get_points() < 100:
            self.take_turns() 
            self.show_scores()
        return

    def setup(self):
        #print("New round started.")
        self.knocked = False

        for player in self.players:
            while player.hand_size() > 0:
                player.drop(player.hand[-1])

        self.deck = Deck()
        self.deck.shuffle()
        #self.deck.show()

        for _ in range(3):
            for player in self.players:
                player.pull()
            #player.show()

        self.pile = Pile()
        self.pile.put(self.deck.draw())
        #self.pile.show()
        return


    def show(self):
        print(f"PILE: {self.pile.cards[-1].rank} of {SUITS[self.pile.cards[-1].suit]}")
        print(f"Size of deck: {len(self.deck.cards)}")

    def take_turns(self):
        for player in self.players:
            if self.deck.get_size() == 0:
                self.deck.new_from_pile(self.pile)
                self.deck.shuffle()
            if self.knocked != player:
                player.take_turn(self.pile)
            else:
                self.end_round()
                return
        #self.show()
        return

    def end_round(self):
        winner = None
        tally = 0
        for p, player in enumerate(self.players):
            if max(player.tally()) > tally:
                winner = p
                tally = max(player.tally())
        self.players[winner].give_point()
        
        #print(f"Player {winner+1} wins with a score of {max(self.players[winner].tally())}!")
        self.setup()
        return

    def show_scores(self):
        print(f"The scores are:")
        for i, player in enumerate(self.players):
            print(f"Player {i+1}: {player.get_points()}")

    def knock(self, player):
        if not self.knocked:
            self.knocked = player
        return

def start_game():
    game = Game_31()
start_game()

# Testing different strategies for the card game 31

from cardgame_setup import Game, Deck, Card, SUITS
import game_31_knock_immediately
import game_31_knock_over_x
import game_31_knock_over_20
import game_31_knock_over_20_toss_best

class Player:
    def __init__(self, game, strategy = game_31_knock_immediately.strategy, name="Nameless soulless player", points = 0):
        self.name = name
        self.game = game
        self.points = points
        self.hand = []
        self.strategy = strategy

    def pull(self, discard = False):
        if discard:
            self.hand.append(self.game.discard.get())
        else:
            self.hand.append(self.game.deck.draw())
        return
    
    def drop(self, card):
        self.hand.remove(card)
        self.game.discard.put(card)
        return

    def hand_size(self):
        return len(self.hand)

    def knock(self):
        self.game.knock(self)
        return

    def take_turn(self, discard):
        self.strategy(self, discard)
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

class Discard:
    def __init__(self, cards = []):
        self.cards = cards
        return

    def put(self, card):
        self.cards.append(card)
        return

    def get(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def peek(self):
        if len(self.cards) == 0:
            return None
        return self.cards[-1]

    def show(self):
        if len(self.cards) == 0:
            print("-~= PILE =~-")
            print("PILE EMPTY :(")
            print("-~=\PILE =~-")
            return "Ok"
        print("-~= PILE =~-")
        print(f"{self.cards[-1].rank} of {SUITS[self.cards[-1].suit]}")
        print("-~=\PILE =~-")
        return "Ok"

class Game_31(Game):
    def __init__(self):
        print("New game started.") 
        
        player1_strat = lambda self, discard : game_31_knock_over_x.strategy(self, discard,20)
        player2_strat = lambda self, discard : game_31_knock_over_x.strategy(self, discard,20)
        player3_strat = lambda self, discard : game_31_knock_over_x.strategy(self, discard,20)
        player4_strat = lambda self, discard : game_31_knock_over_x.strategy(self, discard,20)
        player1 = Player(self, player1_strat, "Måns")
        player2 = Player(self, player2_strat, "August")
        player3 = Player(self, player3_strat, "Jesaja")
        player4 = Player(self, player4_strat)
        self.players = [player1, player2, player3, player4]
        
        self.setup()
        
        while self.players[1].get_points() < 10000:
            self.take_turns() 
        self.show_scores()
        return

    def setup(self):
        #print("New round started.")
        self.knocked = False

        self.shuffle(self.players)

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

        self.discard = Discard()
        self.discard.put(self.deck.draw())
        #self.discard.show()
        return


    def show(self):
        print(f"PILE: {self.discard.cards[-1].rank} of {SUITS[self.discard.cards[-1].suit]}")
        print(f"Size of deck: {len(self.deck.cards)}")
        for i, player in enumerate(self.players):
            print(f"Player {i+1} has ", end = "")
            for card in player.hand:
                print(f"{card.rank} of {SUITS[card.suit]} ",end="")
            print("")

    def take_turns(self):
        for player in self.players:
            if self.deck.get_size() == 0:
                self.end_round(tie=True)
            if self.knocked != player:
                player.take_turn(self.discard)
            else:
                self.end_round()
                return
            #self.show()
        return

    def end_round(self, tie = False):
        if not tie:
            #print("Someone won!")
            winner = None
            tally = 0
            for p, player in enumerate(self.players):
                if max(player.tally()) > tally:
                    winner = p
                    tally = max(player.tally())
            self.players[winner].give_point()
        else:  
            print("Noone won!")
        #print(f"Player {winner+1} wins with a score of {max(self.players[winner].tally())}!")
        self.setup()
        return

    def show_scores(self):
        print(f"The scores are:")
        for player in self.players:
            print(f"{player.name}: {player.get_points()}")

    def knock(self, player):
        if not self.knocked:
            self.knocked = player
        return

def start_game():
    game = Game_31()

start_game()
